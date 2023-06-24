from discord.ext import commands
import discord
import os, asyncio
from Utils import db
from Utils.config import TOKEN, STATUS
db.init()


def get_prefix(bot, message):
    return db.get_guild_prefix(message.guild.id)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=get_prefix, intents=intents)
bot.remove_command("help")

print(f"""     _       _             ____   ____ _______
    | |     | |           |  _ \ / __ \__   __|
  __| | __ _| |__  _   _  | |_) | |  | | | |
 / _` |/ _` | '_ \| | | | |  _ <| |  | | | |
| (_| | (_| | |_) | |_| | | |_) | |__| | | |
 \__,_|\__,_|_.__/ \__,_| |____/ \____/  |_|
""")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(STATUS))
    print('>────────────────────────<')
    print('Logged as:')
    print('Name: {0.user.name}'.format(bot))
    print('ID: {0.user.id}'.format(bot))
    print('>────────────────────────<')

async def load_extensions():
    for filename in os.listdir("./Modules"):
        if filename.endswith(".py"):
            await bot.load_extension(f"Modules.{filename[:-3]}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)

asyncio.run(main())