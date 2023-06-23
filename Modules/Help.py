import discord
from discord.ext import commands

from db.db import get_guild_prefix
from main import FOOTER, ICON

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['?'])
    async def help(self,ctx, command=None):
        prefix = get_guild_prefix(ctx.guild.id)
      
        if not command:
            helpcommands=discord.Embed(title="ᕼᗴᒪᕈ", description="", color=0x00ff00)
            helpcommands.add_field(name=f":exclamation: `{prefix}help info`", value="info commands", inline=True)
            helpcommands.add_field(name=f":name_badge: `{prefix}help mod`", value="moderation commands", inline=True)
            helpcommands.add_field(name=f"<a:fun:863113337948078110> `{prefix}help fun`", value="fun commands", inline=True)
            helpcommands.add_field(name=f":camera: `{prefix}help image`", value="image commands", inline=True)
            helpcommands.add_field(name=f"`{prefix}help welcome`", value="welcomer commands", inline=True)
            helpcommands.add_field(name=f"<a:giveway:863110974918754365> `{prefix}help giveaway`", value="giveaway commands", inline=True)
            helpcommands.add_field(name=f":gear: `{prefix}help config`", value="config commands", inline=True)
            helpcommands.set_footer(text=FOOTER, icon_url=ICON)

        if command == "info":
            helpcommands=discord.Embed(title=":exclamation: Info commands", description="", color=0x00ff00)
            helpcommands.add_field(name=f"`{prefix}ping`", value="bot ping", inline=True)          
            helpcommands.add_field(name=f"`{prefix}serverinfo`", value="server info", inline=True)
            helpcommands.set_footer(text=FOOTER, icon_url=ICON)

        if command == "mod":
            helpcommands = discord.Embed(title=":name_badge: Moderation Help",description="",color=0x00ff00)
            helpcommands.add_field(name=f"`{prefix}kick <@name>`",value="kick member",inline=True)
            helpcommands.add_field(name=f"`{prefix}ban <@name> <reason>`",value="ban user",inline=True)
            helpcommands.add_field(name=f"`{prefix}clear <number>`",value="clear number of messages",inline=True)
            helpcommands.add_field(name=f"`{prefix}mute <@name>`",value="mute user",inline=True)
            helpcommands.add_field(name=f"`{prefix}unmute <@name>`",value="unmute user",inline=True)
            helpcommands.add_field(name=f"`{prefix}addrole <@name> <@role>`",value="add role to user",inline=True)
            helpcommands.add_field(name=f"`{prefix}removerole <@name> <@role>`",value="remove role from user",inline=True)
            helpcommands.add_field(name=f"`{prefix}slowmode <seconds>`",value="set slowmode",inline=True)
            helpcommands.set_footer(text=FOOTER, icon_url=ICON)

        if command == "fun":
            helpcommands = discord.Embed(title="<a:fun:863113337948078110> Fun Help", description="", color=0x00ff00)
            helpcommands.add_field(name=f"`{prefix}pp (@name)`",value="i will show you how long you have peepee",inline=True)
            helpcommands.add_field(name=f"`{prefix}howgay <@name>`",value="how many % is the member gay",inline=True)
            helpcommands.add_field(name=f"`{prefix}say <message>`",value="i will say what you want to say",inline=True)
            helpcommands.add_field(name=f"`{prefix}hack <@name>`",value="i will hack member",inline=True)
            helpcommands.set_footer(text=FOOTER, icon_url=ICON)

        if command == "image":
            helpcommands = discord.Embed(title=":camera: Images Help", description="", color=0x00ff00)
            helpcommands.add_field(name=f"`{prefix}wanted <@name>`", value="This command create wanted foto")
            helpcommands.add_field(name=f"`{prefix}rip <@name>`", value="This command create rip foto")
            helpcommands.set_footer(text=FOOTER, icon_url=ICON)

        if command == "welcome":
            helpcommands = discord.Embed(title="Welcome Help", description="", color=0x00ff00)
            helpcommands.add_field(name=f"`{prefix}setjoinchannel <#channel>`", value="Admin only! set channel for join message")
            helpcommands.add_field(name=f"`{prefix}setleavechannel <#channel>`", value="Admin only! set channel for leave message")
            helpcommands.add_field(name=f"`{prefix}disjoinchannel`", value="Admin only! Disable join channel")
            helpcommands.add_field(name=f"`{prefix}disleavechannel`", value="Admin only! Disable leave channel")
            helpcommands.set_footer(text=FOOTER, icon_url=ICON)

        if command == "config":
            helpcommands = discord.Embed(title=":gear: Config Help", description=f"", color=0x00ff00)
            helpcommands.add_field(name=f"Enable", value=f"`{prefix}setjoinchannel <#channel>` Admin only! set channel for join message\n`{prefix}setleavechannel <#channel>` Admin only! set channel for leave message\n`{prefix}setprefix <prefix>` Admin only! change my prefix on guild", inline=True)
            helpcommands.add_field(name=f"Disable", value=f"`{prefix}disjoinchannel` Admin only! Disable join channel\n`{prefix}disleavechannel` Admin only! Disable leave channel", inline=True)
            helpcommands.set_footer(text=FOOTER, icon_url=ICON)

        if command == "giveaway":
            helpcommands = discord.Embed(title="<a:giveway:863110974918754365>Giveaways Help", description="", color=0x00ff00)
            helpcommands.add_field(name=f"`{prefix}gstart <time> <prize>`", value="Starts giveaway")
            helpcommands.set_footer(text=FOOTER, icon_url=ICON)

        await ctx.send(embed=helpcommands)

async def setup(bot):
    await bot.add_cog(Help(bot))