import discord
import discord.utils
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
import os
from Utils import db
from discord.ext.commands import has_permissions
import requests
from Utils.config import FOOTER, ICON
class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member):
        channelid = db.get_guild_welcomechannel(member.guild.id)
        print(channelid)
        if channelid != None:
            channel = self.bot.get_channel(channelid)
            welcome = Image.open('img/card.png')
            asset = member.display_avatar.with_size(128).url
            r = requests.get(asset)

            data = BytesIO(r.content)
            pfp = Image.open(data)
            pfp = pfp.resize((258, 258))
            welcome.paste(pfp, (421, 62))
            font = ImageFont.truetype("fonts/Minecraft.otf", 35)
            font2 = ImageFont.truetype("fonts/Minecraft.otf", 40)
            d = ImageDraw.Draw(welcome)
            d.text((150, 381), f"{member.name}#{member.discriminator} just joined to the server", fill="white", anchor="ls", font=font2)
            d.text((456, 427), f"Member #{member.guild.member_count}", fill="gray", anchor="ls", font=font)
            welcome.save('img/pcard.png')
            await channel.send(f"Hey {member.mention} welcome to {member.guild.name}!",file = discord.File('img/pcard.png'))
            os.remove('img/pcard.png')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channelid = db.get_guild_leavechannel(member.guild.id)
        if channelid != None:
            channel = self.bot.get_channel(channelid)
            embed=discord.Embed(title=f"{member.name} has left", description=f"on server is {len(list(member.guild.members))} members", color=0xFF0000)
            embed.set_thumbnail(url=f"{member.display_avatar.with_size(128).url}")
            embed.set_footer(text=FOOTER, icon_url=ICON)
            await channel.send(embed=embed)

    @commands.command()
    @has_permissions(administrator=True)
    async def setjoinchannel(self,ctx,*, channel:discord.TextChannel):
        db.update_guild_welcome_channel_id(ctx.guild.id, channel.id)

        await ctx.send(f'Channel changed to: {channel.mention}')

    @commands.command()
    @has_permissions(administrator=True)
    async def setleavechannel(self,ctx,*, channel:discord.TextChannel):
        db.update_guild_leave_channel_id(ctx.guild.id, channel.id)

        await ctx.send(f'Channel changed to: {channel.mention}')

    @commands.command()
    @has_permissions(administrator=True)
    async def disjoinchannel(self,ctx):
        db.update_guild_welcome_channel_id(ctx.guild.id, 0)

        await ctx.send(f'Join channel disabled')

    @commands.command()
    @has_permissions(administrator=True)
    async def disleavechannel(self,ctx):
        db.update_guild_leave_channel_id(ctx.guild.id, 0)

        await ctx.send(f'Leave channel disabled')

async def setup(bot):
    await bot.add_cog(Welcome(bot))