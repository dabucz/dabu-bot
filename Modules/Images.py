import discord
from discord.ext import commands
import requests
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
import os
class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rip(self, ctx, member: discord.Member=None):
      if not member:
        member = ctx.author

      rip = Image.open('img/rip.png')

      asset = member.display_avatar.with_size(128).url
      r = requests.get(asset)

      data = BytesIO(r.content)
      pfp = Image.open(data)
      pfp = pfp.resize((500, 500))
      rip.paste(pfp, (255, 623))
      rip.save('img/prip.png')
      await ctx.send(file = discord.File('img/prip.png'))
      os.remove('img/prip.png')

    @commands.command()
    async def wanted(self, ctx, member: discord.Member=None):
      if not member:
        member = ctx.author

      rip = Image.open('img/wanted.jfif')

      asset = member.display_avatar.with_size(128).url
      r = requests.get(asset)

      data = BytesIO(r.content)
      pfp = Image.open(data)
      pfp = pfp.resize((100, 100))
      rip.paste(pfp, (45, 89))
      rip.save('img/pwanted.png')
      await ctx.send(file = discord.File('img/pwanted.png'))
      os.remove('img/pwanted.png')
async def setup(bot):
    await bot.add_cog(Images(bot))