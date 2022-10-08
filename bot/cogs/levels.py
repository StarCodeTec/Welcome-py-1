from imports.discord       import random, commands, discord, math, Optional
from imports.passcodes     import main
from extras.buttons        import YesNo
from extras.card_generator import Generator
from extras.pages          import BaseButtonPaginator
from wantstoparty._async   import WantsToParty # made this myself(Acacia) :D
from extras                import IDS as ID
from io                    import BytesIO


cafe                   = ID.cafe
XP_PER_LEVEL           = 350
MSG_ATTACHMENT_XP_RATE = 5
EMBED_COLOR            = 0xea69a5
XP_RATE_DEFAULT        = 10

def levelup_msg(msg, lvl, ping=True):
    user = msg.author.mention if ping else msg.author.display_name

    msgs = [
        f"Yay, **{user}** has reached **level {lvl}**! Keep going! <a:woot:917617832655740969>",
        f"Woah, **{user}** has reached **level {lvl}**! Amazing! <a:woohoo:989342765672456222>",
        f"**{user}** has levelled up to **{lvl}**! Keep going! <a:yay:989342786014810215>"
    ]
    
    return msgs

def calculate_level(xp):
    """Calculates a level based on the XP given."""
    return math.trunc(xp / XP_PER_LEVEL)

async def get_xp_rate(msg, data, doublexp=False):
    doublexp = 2 if doublexp else 1 # double XP
    final    = 0
    if msg.channel.id in cafe.roleplaying.channels or data.get("levels", 0) >= 100:
        final += random.randint(1,3) * doublexp # reduced for roleplay channels
    else:
        final += random.randint(2, 8) * doublexp

    if msg.attachments:
        final += MSG_ATTACHMENT_XP_RATE

    return final
    

class Levels(commands.Cog):
    def __init__(self, bot):
        self.bot      = bot
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 2, commands.BucketType.member)
        self.wtp      = WantsToParty(api_key=main.wtp_key, subdomain="femboy")

    @commands.Cog.listener()
    async def on_message(self, msg):
        pg=self.bot.pg
        if msg.author.bot:
            return
        
        if msg.guild.id != ID.server.cafe or not msg.guild: return
        
        bucket      = self.cooldown.get_bucket(msg)
        retry_after = bucket.update_rate_limit()

        if retry_after:
            return # sending messages too quickly - likely spamming.
        
        xp   = pg.RESULT(await self.bot.dpg.fetch_one(query=pg.find('config', '_id'), values={"x": 123}), "config")
        if xp is None:
            await self.bot.dpg.execute(query="INSERT INTO config(_id, xp_rate, doublexp) VALUES (:_id, :xp_rate, :doublexp)", values={"_id": 123, "xp_rate": XP_RATE_DEFAULT, "doublexp": False})

        data = pg.RESULT(await self.bot.dpg.fetch_one(query=pg.find('levels', '_id'), values={"x": msg.author.id}), "levels")
        if msg.channel.id == cafe.media.selfie:
            if not data or data.get("levels", 0) < 3:
                await msg.delete()
                return await msg.author.send("Sorry, you must reach level 3 by chatting before you can post selfies. Thanks for understanding! (Do `/rank` in <#889028781652705350> to see your rank)")

        if data is None:
            upsert={
                    "_id":   msg.author.id,
                    "xp":    1,
                    "level": 0,
                    "ping":  True,
                    "bg":    "https://media.discordapp.net/attachments/956915636582379560/995857644415889508/rank-card.png", 
                    "color": "#1b1b1b"
                }
            await self.bot.dpg.execute(query="INSERT INTO levels(_id, xp, level, ping, bg, color) VALUES (:_id, :xp, :level, :ping, :bg, :color)", values=upsert)
        else:
            xp_rate = await get_xp_rate(msg, data, xp["doublexp"])
        if data is None:
            upsert={
                    "_id":   msg.author.id,
                    "xp":    xp_rate,
                    "level": 0,
                    "ping":  True,
                    "bg":    "https://media.discordapp.net/attachments/956915636582379560/995857644415889508/rank-card.png", 
                    "color": "#1b1b1b"
                }
            await self.bot.dpg.execute(query="INSERT INTO levels(_id, xp, level, ping, bg, color) VALUES (:_id, :xp, :level, :ping, :bg, :color)", values=upsert)
        else:
            current_xp   = data["xp"]
            level_to_get = data["levels"] + 1
            xp_required  = level_to_get * XP_PER_LEVEL
            if current_xp >= xp_required:
                upsert={
                        "_id":   msg.author.id,
                        "xp":    data["xp"] + xp_rate,
                        "level": level_to_get
                    }
                await self.bot.dpg.execute(query=f"UPDATE levels SET xp = {upsert['xp']}, level = {upsert['level']} WHERE _id = {upsert['_id']}")
                
                bot = msg.guild.get_channel(cafe.chat.bot)
                await bot.send(random.choice(levelup_msg(msg, level_to_get, data.get("ping", True))))

            else:
                upsert={
                        "_id":   msg.author.id,
                        "xp":    data["xp"] + xp_rate,
                    }
                await self.bot.dpg.execute(query=f"UPDATE levels SET xp = {upsert['xp']} WHERE _id = {upsert['_id']}")

    @commands.command(hidden=True)
    async def fixlevels(self, ctx):
        """Fixes levels for everyone if there's a change in XPs needed per level."""
        if ctx.guild.id != ID.server.fbc:
            return

        if ctx.author.id != 599059234134687774:
            return

        data = await self.bot.dpg.fetch_all(query= "SELECT * FROM levels")
        msg  = await ctx.send("Working on it...")

        for item in data:
            changed = 0
            actual_level = calculate_level(item.xp)
            if item.level != actual_level:
                await self.bot.dpg.execute(query=f"UPDATE levels SET level = {actual_level} WHERE _id = {item._id})")
                changed += 1

        await msg.edit(f"All done! Updated {changed} members' levels.")
    
    @commands.command(hidden=True)
    @commands.is_owner()
    async def addxp(self, ctx, member: discord.Member, xp: int):
        """(Fenne only) Adds XP to a member."""
        pg     = self.bot.pg
        cur_xp = pg.RESULT(await self.bot.dpg.fetch_one(query=pg.find('levels', '_id'), values={"x": member.id}), "levels")

        if not cur_xp:
            return await ctx.send("I can't do that because they need some XP first.") 

        new_xp      = cur_xp["xp"] + xp
        new_level   = calculate_level(new_xp)

        confirm     = YesNo()
        confirm.ctx = ctx

        msg         = await ctx.send(f"Are you sure you want add to the XP? Their new XP will be **{new_xp}** and new level will be **{new_level}**.", view=confirm)

        await confirm.wait()
        if not confirm.value: return await msg.delete()
        
        await msg.delete()

        if new_level == cur_xp["levels"]:
            await self.bot.dpg.execute(query=f"UPDATE levels SET xp = {new_xp} WHERE _id = {member.id}")

        else:

            await self.bot.dpg.execute(query=f"UPDATE levels SET xp = {new_xp}, level = {new_level} WHERE _id = {member.id}")
        
        await ctx.send(f"Added {xp} XP to {member.display_name}! :tada:")

    @commands.command(hidden=True)
    @commands.is_owner()
    async def removexp(self, ctx, member: discord.Member, xp: int):
        """(Fenne only) Adds XP to a member."""
        pg     = self.bot.pg
        cur_xp = pg.RESULT(await self.bot.dpg.fetch_one(query=pg.find('levels', '_id'), values={"x": member.id}), "levels")

        if not cur_xp:
            return await ctx.send("I can't do that because they need some XP first.") 

        new_xp    = cur_xp["xp"] - xp
        new_level = calculate_level(new_xp)

        if new_xp < 0:
            return await ctx.send("That will make their XP negative and blow the bot up! >:o")

        confirm     = YesNo()
        confirm.ctx = ctx

        msg         = await ctx.send(f"Are you sure you want to remove the XP? Their new XP will be **{new_xp}** and new level will be **{new_level}**.", view=confirm)

        await confirm.wait()
        if not confirm.value: return await msg.delete()
        
        await msg.delete()
        if new_level == cur_xp["levels"]:
            await self.bot.dpg.execute(query=f"UPDATE levels SET xp = {new_xp} WHERE _id = {member.id}")
        else:
            await self.bot.dpg.execute(query=f"UPDATE levels SET xp = {new_xp}, level = {new_level} WHERE _id = {member.id}")

        await ctx.send(f"Removed {xp} XP from {member.display_name}.")


    @commands.hybrid_command(aliases=["level"])
    @discord.app_commands.guilds(ID.server.fbc, ID.server.cafe)
    async def rank(self, ctx:commands.Context, member: discord.Member=None):
        """Shows a members XP and level from talking."""
        pg=self.bot.pg
        member   = member if member else ctx.author

        data     = pg.RESULT(await self.bot.dpg.fetch_one(query=pg.find('levels', '_id'), values={"x": member.id}), "levels")
        all_data = pg.GET_ALL(await self.bot.dpg.fetch_all(query= "SELECT * FROM levels"), "levels")
                
        all_data.sort(key=lambda item: item.get("xp"), reverse=True) # sort ranks in descending order

        index = 1
        for entry in all_data:
            if entry["_id"] == member.id:
                break
            index += 1

        xp      = data["xp"]
        level   = data["levels"]
        lvl_xp  = xp - (level * XP_PER_LEVEL)
        rank    = index
        next_xp = (level * XP_PER_LEVEL) - (level + 1 * XP_PER_LEVEL)
        xp_needed = ((level + 1) * XP_PER_LEVEL) - xp

        if not data.get("bg"):
            if random.randint(0, 3) == 1:
                msg = ":bulb: **Tip:** you can customize your card by changing the background or text color! Use `.card color` or `.card bg`."
            else:
                msg = None
        else:
            msg = None

        card_data = {
            "bg_image": data.get("bg"),
            "profile_image": member.display_avatar.url,
            "level": level,
            "user_xp": lvl_xp,
            "next_xp": XP_PER_LEVEL,
            "xp_needed": xp_needed,
            "user_position": rank,
            "user_name": member.display_name,
            "user_status": member.raw_status,
            "color": data.get("color"),
            "total": xp
        }

        img = Generator().generate_profile(**card_data)

        file = discord.File(fp=img, filename="rank.png")

        await ctx.send(content=msg, file=file)
    
    @commands.group(invoke_without_command=True)
    async def card(self, ctx):
        await ctx.send("Do `.card bg` to change the background or `.card color` to change the color.")
    
    @card.command(aliases=["bg"])
    async def background(self, ctx, reset: Optional[str]="False"):
        if reset.lower() == "reset":
            await self.bot.dpg.execute(query=f"UPDATE levels SET bg = 'https://media.discordapp.net/attachments/956915636582379560/995857644415889508/rank-card.png' WHERE _id = {ctx.author.id}")
            return await ctx.send(f"Reseted!")
        if not ctx.message.attachments or reset != "False":
            return await ctx.send("Please add (attach) an image when using this command! \nOr you can use ``.card background reset`` to reset your current background")
        
        attachment = ctx.message.attachments[0]
        extension  = attachment.filename.split(".")
        extension  = extension[len(extension)-1] 

        file = BytesIO(await attachment.read())
        
        url = await self.wtp.upload_from_bytes(file, extension)

        await self.bot.dpg.execute(query=f"UPDATE levels SET bg = '{url}' WHERE _id = {ctx.author.id}")

        await ctx.send(f"All done!")


    @card.command(aliases=["colour"])
    async def color(self, ctx, hex=None):
        """Changes the colour of the text on the level card."""
        if hex=="reset":
            await self.bot.dpg.execute(query=f"UPDATE levels SET color = '#1b1b1b' WHERE _id = {ctx.author.id}")
            await ctx.send(f"All done! Card **text** color reset")
            return
        if not hex:
            return await ctx.send("To pick the text color, go to <https://rgbacolorpicker.com/hex-color-picker> and copy the hex code at the top.")
        
        if not hex.startswith("#"):
            hex = "#" + str(hex)

        await self.bot.dpg.execute(query=f"UPDATE levels SET color = '{hex}' WHERE _id = {ctx.author.id}")
        await ctx.send(f"All done! Card **text** color set to {hex}")

    @commands.hybrid_command(aliases=["lb"])
    @discord.app_commands.guilds(ID.server.fbc, ID.server.cafe)
    async def leaderboard(self, ctx):
        """Shows the top 15 people on the leaderboard."""
        if ctx.guild.id != ID.server.cafe:
            return await ctx.send("that command doesnt work in this server rn sorry")
        pg   = self.bot.pg
        data = pg.GET_ALL(await self.bot.dpg.fetch_all(query= "SELECT * FROM levels"), "levels")
        data.sort(key=lambda item: item.get("xp"), reverse=True)
        
        out   = []
        place = 1
        for item in data:
            member = ctx.guild.get_member(item["_id"])
            xp     = "{:,}".format(item['xp'])
            if not member:
                return await self.bot.levels.delete(item["_id"])
            if place == 1:
                out.append(f":first_place: {member.mention} {xp} XP (level {item['levels']})")
            elif place == 2:
                out.append(f":second_place: {member.mention} {xp} XP (level {item['levels']})")
            elif place == 3:
                out.append(f":third_place: {member.mention} {xp} XP (level {item['levels']})")
            else:
                out.append(f"**{place}.** {member.mention} {xp} XP (level {item['levels']})")

            place += 1

        class Pages(BaseButtonPaginator):
            async def format_page(self, entries):
                embed = discord.Embed(
                    title="Leaderboard",
                    color=EMBED_COLOR
                )
                embed.description    ="\n".join(entries)
                embed.set_author(name=f"Page {self.current_page}/{self.total_pages}")
                embed.set_footer(text=f"{len(out)} members on the leaderboard.")

                return embed

        await Pages.start(ctx, entries=out, per_page=15)

    @commands.command(hidden=True, name="doublexp")
    @commands.is_owner()
    async def doublexp(self, ctx):
        """(Fenne only) Enables double XP for everyone."""
        pg=self.bot.pg
        data = pg.RESULT(await self.bot.dpg.fetch_one(query=pg.find('config', '_id'), values={"x": 123}), "config")
        if not data["doublexp"]:
            confirm     = YesNo()
            confirm.ctx = ctx
            msg = await ctx.send("**Double XP is not enabled.**\n\nDo you want to enable it?", view=confirm)

            await confirm.wait()
            if confirm.value:
                await self.bot.dpg.execute(query="UPDATE config SET doublexp = True WHERE _id = 123")
                await ctx.send("Double XP has been enabled.")
            await msg.delete()
        
        else:
            confirm     = YesNo()
            confirm.ctx = ctx
            msg         = await ctx.send("**Double XP is enabled.**\n\nDo you want to disable it?", view=confirm)

            await confirm.wait()
            if confirm.value:
                await self.bot.dpg.execute(query="UPDATE config SET doublexp = False WHERE _id = 123")
                await msg.delete()
                await ctx.send("Double XP has been disabled.")
            else:
                await msg.delete()
    
    @commands.hybrid_command(aliases=["howlevelswork"])
    @discord.app_commands.guilds(ID.server.fbc, ID.server.cafe)
    async def howxpworks(self, ctx):
        """Sends a message on how XP works."""
        content = """It works by adding between 2 and 8 XP (at random) every time you send a message (unless double XP is turned on, in which it's... you guessed it, double). Messages containing attachments (images, videos, etc) also get 5 extra XP on top of what you're already getting. XP is reduced to 1-3 in roleplay channels. (double XP still effects it though!)

You gain levels when you reach a number of XP which is a multiple of 350 (350, 700, 1050, etc...)

You can use `.rank` to check your statistics and `.leaderboard` to see who has the most XP in the entire server.

Spamming does not benefit you when it comes to gaining XP as there's a short cooldown period after sending a message. 

**Leaving the server resets your XP!**"""
        e = discord.Embed(title="How levels work", color=EMBED_COLOR)
        e.description = content
        e.set_footer(text="Levels by acatia#5378 :)")

        await ctx.send(embed=e)

    @commands.hybrid_command()
    @discord.app_commands.guilds(ID.server.fbc, ID.server.cafe)
    async def toggleping(self, ctx:commands.Context):
        """Enables/disables pings when you level up. This will still send the level up message."""
        pg=self.bot.pg
        data = pg.RESULT(await self.bot.dpg.fetch_one(query=pg.find('levels', '_id'), values={"x": ctx.author.id}), "levels")

        if data.get("ping", True) == True:
            to_send = "You are currently being pinged for level up messages.\n\n**Do you want to disable level-up pings?**"
        else:
            to_send = "You currently aren't being pinged for level up messages.\n\n**Do you want to be pinged again?**"
        
        confirm = YesNo()
        confirm.ctx = ctx

        msg = await ctx.send(to_send, view=confirm)

        await confirm.wait()
        if not confirm.value:
            return await msg.edit(content="Cancelled.")
        
        if confirm.value:
            if data.get("ping") == True:
                await self.bot.dpg.execute(query=f"UPDATE levels SET ping = False WHERE _id = {ctx.author.id}")
            else:
                await self.bot.dpg.execute(query=f"UPDATE levels SET ping = True WHERE _id = {ctx.author.id}")

        await msg.edit(content="Your settings have been changed!", view=confirm.stop())
    
    @commands.hybrid_command(aliases=["levelstatus"])
    @discord.app_commands.guilds(ID.server.fbc, ID.server.cafe)
    async def xpstatus(self, ctx: commands.Context):
        """Shows the current status on the levelling system."""
        data = self.bot.pg.RESULT(await self.bot.dpg.fetch_one(query=self.bot.pg.find('config', '_id'), values={"x": 123}), "config")
        if data["doublexp"] == True:
            doublexp = "Enabled - chatting will give you double XP"
        else:
            doublexp = "Disabled - XP is not doubled."
        
        content = f"XP is random per-message. You get between 2 and 8 XP.\nSending media is a 5 XP bonus!\n\nDouble XP: {doublexp}"

        e = discord.Embed(color=EMBED_COLOR, title="XP Status")
        e.description = content

        await ctx.send(embed=e)
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        ex=[760928339589726209]
        if member.id in ex:
            return
        try:
            await self.bot.dpg.execute(query=f"DELETE FROM levels WHERE _id = {member.id}")
        except:
            pass