import os
import json
from discord.ext import commands
import discord
from flask import Flask
from threading import Thread
from db import db
db.init()

with open("config.json") as f:
    config = json.load(f)

host = config.get("host")
uname = config.get("username")
password = config.get("password")
db_name = config.get("db_name")

def get_prefix(bot, message):
    return db.get_guild_prefix(message.guild.id)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=get_prefix, intents=intents)
bot.remove_command("help")

TOKEN = config.get("token")
STATUS = config.get("status")
FOOTER = config.get("footer")
ICON = config.get('icon_url')

print(f"""     _       _             ____   ____ _______
    | |     | |           |  _ \ / __ \__   __|
  __| | __ _| |__  _   _  | |_) | |  | | | |
 / _` |/ _` | '_ \| | | | |  _ <| |  | | | |
| (_| | (_| | |_) | |_| | | |_) | |__| | | |
 \__,_|\__,_|_.__/ \__,_| |____/ \____/  |_|
""")

@bot.event
async def on_ready():

    with open('modules.json', 'r') as f:
        modules = json.load(f)

    await bot.load_extension("Modules.Events")
    await bot.load_extension("Modules.Help")

    info = modules["Info"]
    mod = modules["Moderation"]
    fun = modules["Fun"]
    images = modules["Images"]
    welcome = modules["Welcome"]
    gw = modules["Giveaways"]

    await bot.change_presence(activity=discord.Game(STATUS))
    print('>────────────────────────<')
    print('Logged as:')
    print('Name: {0.user.name}'.format(bot))
    print('ID: {0.user.id}'.format(bot))
    print('>────────────────────────<')
    print('')
    print('>────────────────────────<')
    print('Loaded Modules:')

    if info == "True":
        await bot.load_extension("Modules.Info")
        print("Module Info")

    if mod == "True":
        await bot.load_extension("Modules.Mod")
        print("Module Modearation")

    if fun == "True":
        await bot.load_extension("Modules.Fun")
        print("Module Fun")

    if images == "True":
        await bot.load_extension("Modules.Images")
        print("Module Images")

    if welcome == "True":
        await bot.load_extension("Modules.Welcome")
        print("Module Welcome")

    if gw == "True":
        await bot.load_extension("Modules.Giveaways")
        print("Module Giveaways")

    print('>────────────────────────<')


bot.run(TOKEN)