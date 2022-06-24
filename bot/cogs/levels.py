import discord
import random
import extras.IDS as ID
from extras.buttons import YesNo
from discord.ext import commands

def levelup_msg(msg, lvl):
    user = msg.author.mention

    ending_note = f"\n*Do `.rank` in <#{ID.cafe.chat.bot}> to see your rank*"
    msgs = [
        f"Yay, {user} has reached **level {lvl}**! Keep going! <a:woot:917617832655740969>{ending_note}",
        f"Woah, {user} has reached **level {lvl}**! Amazing! <a:woohoo:989342765672456222>{ending_note}",
        f"{user} has levelled up to {lvl}! Keep on going! <a:yay:989342786014810215>{ending_note}"
    ]
    
    return msgs

class Levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cooldown = commands.CooldownMapping.from_cooldown(1, 2, commands.BucketType.member)
        
        self.xp_rate = 10
        self.msg_attachment_xp_rate = 20

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
        
        if not xp or not xp.get("xp_rate"):
            await self.bot.config.upsert({"_id": 123, "xp_rate": self.xp_rate, "doublexp": False})

        xp_rate = xp["xp_rate"]

        data = await self.bot.levels.find(msg.author.id)

        xp_rate = self.xp_rate if not xp["doublexp"] else self.xp_rate * 2        

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
            xp_required = level_to_get * 100
            
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


    @commands.command(aliases=["level"])
    async def rank(self, ctx, member: discord.Member=None):
        """Shows a members XP and level from talking."""
        member = member if member else ctx.author
        
        if member == ctx.author:
            embed = discord.Embed(
                color=0xf4c2c2,
                title="Your rank"
            )
        else:
            embed = discord.Embed(
                color=0xf4c2c2,
                title=f"{member.name}'s rank"
            )

        data = await self.bot.levels.find(member.id)
        all_data = await self.bot.levels.get_all()

        if not data:
            embed.description = "You don't have a level currently. Let's start talking!"
            return await ctx.send(embed=embed)
        
        all_data.sort(key=lambda item: item.get("xp"), reverse=True) # sort ranks in descending order

        index = 1
        for entry in all_data:
            if entry["_id"] == member.id:
                break
            index += 1

        xp = data["xp"]
        level = data["level"]
        xp_needed = ((level + 1) * 100) - xp # amount of xp needed to advance a level
        rank = index
        all_ranks = len(all_data)

        embed.add_field(name="Level:", value=f"Level {level}", inline=False)
        embed.add_field(name="XP:", value=f"{xp} XP\n{xp_needed} to get {level + 1}", inline=False)
        embed.add_field(name="Rank:", value=f"Your rank is **{rank}/{all_ranks}**")
        embed.set_footer(text="Do .leaderboard to see the leaderboard!")

        await ctx.send(embed=embed)

    @commands.command(aliases=["lb"])
    async def leaderboard(self, ctx):
        """Shows the top 15 people on the leaderboard."""
        if ctx.guild.id != ID.server.cafe:
            return await ctx.send("that command doesnt work here rn sorry about that")

        data = await self.bot.levels.get_all()
        data.sort(key=lambda item: item.get("xp"), reverse=True)
        
        out = []
        place = 1
        for item in data:
            member = ctx.guild.get_member(item["_id"])
            if place == 1:
                out.append(f":first_place: {member.mention} {item['xp']} XP (level {item['level']})")
            elif place == 2:
                out.append(f":second_place: {member.mention} {item['xp']} XP (level {item['level']})")
            elif place == 3:
                out.append(f":third_place: {member.mention} {item['xp']} XP (level {item['level']})")
            else:
                out.append(f"**{place}.** {member.mention} {item['xp']} XP (level {item['level']})")

            if place == 15:
                break

            place += 1

        to_send = "\n".join(out)

        embed = discord.Embed(
            color=0xf4c2c2,
            title="Leaderboard",
            description=to_send
        )
        embed.set_footer(text="Showing the top 15 people")

        await ctx.send(embed=embed)

    @commands.command(hidden=True, name="doublexp")
    @commands.is_owner()
    async def doublexp(self, ctx):
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
