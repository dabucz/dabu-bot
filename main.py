import os
import json
from discord.ext import commands
import discord
from dotenv import load_dotenv
from flask import Flask
from threading import Thread

load_dotenv()

def get_prefix(bot, message):
    with open('db/prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=get_prefix, intents=intents)
bot.remove_command("help")

TOKEN = os.getenv("TOKEN")
STATUS = os.getenv("STATUS")
FOOTER = os.getenv("FOOTER")
ICON = os.getenv('ICON_URL')

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

    bot.load_extension("Modules.Events")
    bot.load_extension("Modules.Help")

    info = modules["Info"]
    mod = modules["Moderation"]
    fun = modules["Fun"]
    images = modules["Images"]
    welcome = modules["Welcome"]
    sug = modules["Suggestions"]
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
        bot.load_extension("Modules.Info")
        print("Module Info")

    if mod == "True":
        bot.load_extension("Modules.Mod")
        print("Module Modearation")

    if welcome == "True":
        print("Module Welcome")

    if fun == "True":
        bot.load_extension("Modules.Fun")
        print("Module Fun")

    if images == "True":
        bot.load_extension("Modules.Images")
        print("Module Images")

    if welcome == "True":
        bot.load_extension("Modules.Welcome")
        print("Module Welcome")

    if sug == "True":
        bot.load_extension("Modules.Suggestions")
        print("Module Suggestions")

    if gw == "True":
        bot.load_extension("Modules.Giveaways")
        print("Module Giveaways")

    print('>────────────────────────<')

app = Flask('')

@app.route('/')
def home():
    return "I'm alive"

def run():
  app.run(host='0.0.0.0',port=3216)

t = Thread(target=run)
t.start()

from discord.ext import tasks
import json

@tasks.loop(seconds = 20)
async def api():
    with open('api/data.json', 'r') as f:
        data = json.load(f)
    members = 0
    channels = 0
    for item in bot.guilds:
        members += item.member_count
    for guild in bot.guilds:
        for channel in guild.text_channels:
            channels += 1
    for guild in bot.guilds:
        for channel in guild.voice_channels:
            channels += 1

        
    data["guilds"] = f"{len(list(bot.guilds))}"
    data["members"] = f"{members}"
    data["channels"] = f"{channels}"

    with open('api/data.json', 'w') as f:
        json.dump(data, f, indent=4)

api.start()

bot.run(TOKEN)
