import discord
import random
import math
import extras.IDS as ID
from extras.buttons import YesNo
from extras.card_generator import Generator
from extras.pages import BaseButtonPaginator
from passcodes import main
from discord.ext import commands
from wantstoparty._async import WantsToParty # made this myself :D
from io import BytesIO

XP_PER_LEVEL = 350
MSG_ATTACHMENT_XP_RATE = 5

def levelup_msg(msg, lvl):
    user = msg.author.mention

    msgs = [
        f"Yay, {user} has reached **level {lvl}**! Keep going! <a:woot:917617832655740969>",
        f"Woah, {user} has reached **level {lvl}**! Amazing! <a:woohoo:989342765672456222>",
        f"{user} has levelled up to {lvl}! Keep on going! <a:yay:989342786014810215>"
    ]
    
    return msgs

def calculate_level(xp):
    """Calculates a level based on the XP given."""
    return math.trunc(xp / XP_PER_LEVEL)

class Levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 2, commands.BucketType.member)
    
        self.msg_attachment_xp_rate = 5

        self.wtp = WantsToParty(api_key=main.wtp_key, subdomain="femboy")

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author.bot:
            return
        
        if msg.guild.id != ID.server.cafe or not msg.guild:
            return
        
        bucket = self.cooldown.get_bucket(msg)
        retry_after = bucket.update_rate_limit()

        if retry_after:
            return # sending messages too quickly - likely spamming.
        
        xp = await self.bot.config.find(123)
        
        rand_xp = random.randint(2, 8)

        if not xp:
            await self.bot.config.upsert({"_id": 123, "doublexp": False})

        data = await self.bot.levels.find(msg.author.id)

        if msg.channel.id == ID.cafe.media.selfie:
            if not data or data.get("level", 0) < 3:
                await msg.delete()
                return await msg.author.send("You must reach level 3 by chatting before you can post selfies. Thanks for understanding!")

        xp_rate = rand_xp if not xp["doublexp"] else rand_xp * 2

        if not data:
            await self.bot.levels.upsert(
                {
                    "_id": msg.author.id,
                    "xp": xp_rate,
                    "level": 0
                }
            )
        else:
            current_xp = data["xp"]
            level_to_get = data["level"] + 1
            xp_required = level_to_get * XP_PER_LEVEL
            
            if current_xp >= xp_required:
                await self.bot.levels.upsert(
                    {
                        "_id": msg.author.id,
                        "xp": data["xp"] + xp_rate if not msg.attachments else data["xp"] + self.msg_attachment_xp_rate,
                        "level": level_to_get
                    }
                )
                
                bot = msg.guild.get_channel(ID.cafe.chat.bot)
                await bot.send(random.choice(levelup_msg(msg, level_to_get)))
            else:
                await self.bot.levels.upsert(
                    {
                        "_id": msg.author.id,
                        "xp": data["xp"] + xp_rate if not msg.attachments else data["xp"] + self.msg_attachment_xp_rate
                    }
                )

    @commands.command(hidden=True)
    async def fixlevels(self, ctx):
        """Fixes levels for everyone if there's a change in XPs needed per level."""
        if ctx.guild.id != ID.server.fbc:
            return

        if ctx.author.id != 599059234134687774:
            return

        data = await self.bot.levels.get_all()

        msg = await ctx.send("Working on it...")
        for item in data:
            changed = 0
            actual_level = calculate_level(item["xp"])
            if item["level"] != actual_level:
                await self.bot.levels.upsert(
                    {
                        "_id": item["_id"],
                        "xp": item["xp"],
                        "level": actual_level
                    }
                )
                changed += 1

        await msg.edit(f"All done! Updated {changed} members' levels.")
    
    @commands.command(hidden=True)
    @commands.is_owner()
    async def addxp(self, ctx, member: discord.Member, xp: int):
        """(Fenne only) Adds XP to a member."""
        cur_xp = await self.bot.levels.find(member.id)

        if not cur_xp:
            return await ctx.send("I can't do that because they need some XP first.") 

        new_xp = cur_xp["xp"] + xp
        new_level = calculate_level(new_xp)

        confirm = YesNo()
        confirm.ctx = ctx

        msg = await ctx.send(f"Are you sure you want add to the XP? Their new XP will be **{new_xp}** and new level will be **{new_level}**.", view=confirm)

        await confirm.wait()
        if not confirm.value:
            return await msg.delete()
        
        await msg.delete()

        await self.bot.levels.upsert(
            {
                "_id": member.id,
                "xp": new_xp,
                "level": new_level
            }
        )
        await ctx.send(f"Added {xp} XP to {member.display_name}! :tada:")

    @commands.command(hidden=True)
    @commands.is_owner()
    async def removexp(self, ctx, member: discord.Member, xp: int):
        """(Fenne only) Adds XP to a member."""
        cur_xp = await self.bot.levels.find(member.id)

        if not cur_xp:
            return await ctx.send("I can't do that because they need some XP first.") 

        new_xp = cur_xp["xp"] - xp
        new_level = calculate_level(new_xp)

        if new_xp < 0:
            return await ctx.send("That will make their XP negative and blow the bot up! >:o")

        confirm = YesNo()
        confirm.ctx = ctx

        msg = await ctx.send(f"Are you sure you want to remove the XP? Their new XP will be **{new_xp}** and new level will be **{new_level}**.", view=confirm)

        await confirm.wait()
        if not confirm.value:
            return await msg.delete()
        
        await msg.delete()

        await self.bot.levels.upsert(
            {
                "_id": member.id,
                "xp": new_xp,
                "level": new_level
            }
        )
        await ctx.send(f"Removed {xp} XP from {member.display_name}.")


    @commands.command(aliases=["level"])
    async def rank(self, ctx, member: discord.Member=None):
        """Shows a members XP and level from talking."""
        member = member if member else ctx.author

        data = await self.bot.levels.find(member.id)
        all_data = await self.bot.levels.get_all()

        
        all_data.sort(key=lambda item: item.get("xp"), reverse=True) # sort ranks in descending order

        index = 1
        for entry in all_data:
            if entry["_id"] == member.id:
                break
            index += 1

        xp = data["xp"]
        level = data["level"]
        lvl_xp = xp - (level * XP_PER_LEVEL)
        rank = index
        next_xp = (level * XP_PER_LEVEL) - (level + 1 * XP_PER_LEVEL)
        xp_needed = ((level + 1) * XP_PER_LEVEL) - xp

        card_data = {
            "bg_image": data.get("bg") if data.get("bg") else "https://media.discordapp.net/attachments/956915636582379560/995857644415889508/rank-card.png", # change to bg when fen gives it
            "profile_image": member.display_avatar.url,
            "level": level,
            "user_xp": lvl_xp,
            "next_xp": XP_PER_LEVEL,
            "xp_needed": xp_needed,
            "user_position": rank,
            "user_name": member.name,
            "user_status": member.raw_status,
            "color": data.get("color") if data.get("color") else "#1b1b1b",
            "total": xp
        }

        img = Generator().generate_profile(**card_data)

        file = discord.File(fp=img, filename="rank.png")

        await ctx.send(file=file)   
    
    @commands.group(invoke_without_command=True)
    async def card(self, ctx):
        await ctx.send("Do `.card bg` to change the background or `.card color` to change the color.")
    
    @card.command(aliases=["bg"])
    async def background(self, ctx):
        if not ctx.message.attachments:
            return await ctx.send("Please add (attach) an image when using this command!")
        
        attachment = ctx.message.attachments[0]
        extension = attachment.filename.split(".")
        extension = extension[len(extension)-1] 

        file = BytesIO(await attachment.read())
        
        url = await self.wtp.upload_from_bytes(file, extension)

        await self.bot.levels.upsert({"_id": ctx.author.id, "bg": str(url)})

        await ctx.send(f"All done!")


    @card.command(aliases=["colour"])
    async def color(self, ctx, hex=None):
        """Changes the colour of the text on the level card."""
        if not hex:
            return await ctx.send("To pick the text color, go to <https://rgbacolorpicker.com/hex-color-picker> and copy the hex code at the top.")
        
        if not hex.startswith("#"):
            hex = "#" + str(hex)

        await self.bot.levels.upsert({"_id": ctx.author.id, "color": hex})
        await ctx.send(f"All done! Card **text** color set to {hex}")

    @commands.command(aliases=["lb"])
    async def leaderboard(self, ctx):
        """Shows the top 15 people on the leaderboard."""
        if ctx.guild.id != ID.server.cafe:
            return await ctx.send("that command doesnt work in this server rn sorry")

        data = await self.bot.levels.get_all()
        data.sort(key=lambda item: item.get("xp"), reverse=True)
        
        out = []
        place = 1
        for item in data:
            member = ctx.guild.get_member(item["_id"])
            if not member:
                return await self.bot.levels.delete(item["_id"])
            if place == 1:
                out.append(f":first_place: {member.mention} {item['xp']} XP (level {item['level']})")
            elif place == 2:
                out.append(f":second_place: {member.mention} {item['xp']} XP (level {item['level']})")
            elif place == 3:
                out.append(f":third_place: {member.mention} {item['xp']} XP (level {item['level']})")
            else:
                out.append(f"**{place}.** {member.mention} {item['xp']} XP (level {item['level']})")

            place += 1

        class Pages(BaseButtonPaginator):
            async def format_page(self, entries):
                embed = discord.Embed(
                    title="Leaderboard",
                    color=0xf4c2c2
                )
                embed.description = "\n".join(entries)
                embed.set_author(name=f"Page {self.current_page}/{self.total_pages}")

                return embed

        await Pages.start(ctx, entries=out, per_page=15)

    @commands.command(hidden=True, name="doublexp")
    @commands.is_owner()
    async def doublexp(self, ctx):
        """(Fenne only) Enables double XP for everyone."""
        data = await self.bot.config.find(123)
        if not data["doublexp"]:
            confirm = YesNo()
            confirm.ctx = ctx
            msg = await ctx.send("**Double XP is not enabled.**\n\nDo you want to enable it?", view=confirm)

            await confirm.wait()
            if confirm.value:
                await self.bot.config.upsert({"_id": 123, "doublexp": True})
                await msg.delete()
                await ctx.send("Double XP is now enabled! <a:yay:989342786014810215>")
            else:
                await msg.delete()
        
        else:
            confirm = YesNo()
            confirm.ctx = ctx
            msg = await ctx.send("**Double XP is enabled.**\n\nDo you want to disable it?", view=confirm)

            await confirm.wait()
            if confirm.value:
                await self.bot.config.upsert({"_id": 123, "doublexp": False})
                await msg.delete()
                await ctx.send("Double XP has been disabled.")
            else:
                await msg.delete()
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        ex=[760928339589726209]
        if member.id in ex:
            return
        try:
            await self.bot.levels.delete(member.id)
        except:
            pass