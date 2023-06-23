from discord.ext import commands
from dotenv import load_dotenv
from db import db

from main import DEFAULT_PREFIX

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        db.register_guild(guild.id, default_prefix)

    @commands.Cog.listener()
    async def on_guild_remove(self,guild):
        db.remove_guild(guild.id)

    @commands.Cog.listener(name='on_command')
    async def print(self, ctx):
        server = ctx.guild.name
        user = ctx.author
        command = ctx.command
        with open("cmd_log.txt", "a", encoding="utf-8") as f:
            f.write(f"{server} > {user} > {command}\n")

async def setup(bot):
    await bot.add_cog(Events(bot))