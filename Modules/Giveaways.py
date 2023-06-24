import discord
import asyncio
from discord.ext import commands
import random

from discord.ext.commands import has_permissions

from Utils.config import ICON

class Giveaways(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['gw', 'gs'])
    @has_permissions(manage_messages=True)
    async def gstart(self,ctx, time=None, *, prize=None):
        if time == None:
            return await ctx.send(embed=discord.Embed(title=f"Please include time", description=f"", color=discord.Color.red()))
        elif prize == None:
            return await ctx.send(embed=discord.Embed(title=f"Please include prize!", description=f"", color=discord.Color.red()))
        embed = discord.Embed(title=f"{prize}", description=f"React with <a:giveway:863110974918754365> to enter!\nEnds: in {time}\nHosted by: {ctx.author.mention}", color=0x00FF00)
        time_convert = {"s":1, "m":60, "h":3600, "d":86400}
        gawtime = int(time[0]) * time_convert[time[-1]]
        embed.set_footer(text=f"Giveaway ends in {time}", icon_url=ICON)
        gaw_msg = await ctx.send(embed=embed)

        await gaw_msg.add_reaction("🎉")
        await asyncio.sleep(gawtime)

        new_gaw_msg = await ctx.channel.fetch_message(gaw_msg.id)
        users = [user async for user in new_gaw_msg.reactions[0].users()]
        users.pop(users.index(self.bot.user))
        winner = random.choice(users)
        new_em = discord.Embed(title=f"{prize}", description=f"Winner: {winner.mention}\nHosted by: {ctx.author.mention}", color=0x00FF00)
        new_em.set_footer(text=f"Giveaway ended", icon_url=ICON)
        await gaw_msg.edit(embed=new_em)
        await ctx.send(f"{winner.mention} has won the giveaway for **{prize}**!")

async def setup(bot):
    await bot.add_cog(Giveaways(bot))