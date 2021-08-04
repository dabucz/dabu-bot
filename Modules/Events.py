from discord.ext import commands
import json

from dotenv import load_dotenv
import os

load_dotenv()

DEFAULT_PREFIX = os.getenv('DEFAULT_PREFIX')

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self,guild): #when the bot joins the guild
        with open('db/prefixes.json', 'r') as f: #read the prefix.jsonfile
            prefixes = json.load(f) #load the json file
        prefixes[str(guild.id)] = '.'

        with open('db/prefixes.json', 'w') as f: #write in the prefix.json "message.guild.id": "bl!"
            json.dump(prefixes, f, indent=4) #the indent is to make everything look a bit neater
        #join msg

        with open('db/welcomer/joinch_id.json', 'r') as f:
            chid = json.load(f) 

        chid[str(guild.id)] = 'None'

        with open('db/welcomer/joinch_id.json', 'w') as f:
            json.dump(chid, f, indent=4)

        with open('db/welcomer/leavech_id.json', 'r') as f:
            lchid = json.load(f) 

        lchid[str(guild.id)] = 'None'

        with open('db/welcomer/leavech_id.json', 'w') as f:
            json.dump(lchid, f, indent=4)
        #suggestions
        with open('db/sugchid.json', 'r') as f:
            chid = json.load(f) 

        chid[str(guild.id)] = 'None'

        with open('db/sugchid.json', 'w') as f:
            json.dump(chid, f, indent=4)

    @commands.Cog.listener()
    async def on_guild_remove(self,guild): #when the bot is removed frothe guild
        with open('db/prefixes.json', 'r') as f: #read the file
            prefixes = json.load(f)

        prefixes.pop(str(guild.id)) #find the guild.id that bot waremoved from

        with open('db/prefixes.json', 'w') as f: #deletes the guild.ias well as its prefix
            json.dump(prefixes, f, indent=4)
        #join msg
        with open('db/welcomer/joinch_id.json', 'r') as f:
            chid = json.load(f)

        chid.pop(str(guild.id))

        with open('db/welcomer/joinch_id.json', 'w') as f:
            json.dump(chid, f, indent=4)


        with open('db/welcomer/leavech_id.json', 'r') as f:
            lchid = json.load(f)

        lchid.pop(str(guild.id))

        with open('db/welcomer/leavech_id.json', 'w') as f:
            json.dump(lchid, f, indent=4)
        #suggestions
        with open('db/sugchid.json', 'r') as f:
            chid = json.load(f)

        chid.pop(str(guild.id))

        with open('db/sugchid.json', 'w') as f:
            json.dump(chid, f, indent=4) 

    @commands.Cog.listener(name='on_command')
    async def print(self, ctx):
        server = ctx.guild.name
        user = ctx.author
        command = ctx.command
        with open("cmd_log.txt", "a", encoding="utf-8") as f:
            f.write(f"{server} > {user} > {command}\n")



def setup(bot):
    bot.add_cog(Events(bot))