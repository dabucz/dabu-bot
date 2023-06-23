from discord.ext import commands
import os
import discord
from main import FOOTER, ICON

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

    @commands.command()
    async def serverinfo(self,ctx):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)

        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        memberCount = str(ctx.guild.member_count)
        icon = str(ctx.guild.icon)


        embed = discord.Embed(title=name + " Server Information",description=description,color=0x00ff00)
        if icon != None: embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=id, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)

        await ctx.send(embed=embed)
        
async def setup(bot):
    await bot.add_cog(Info(bot))