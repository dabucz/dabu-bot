import mysql.connector
from Utils.config import mysql_config

host = mysql_config.get("host")
uname = mysql_config.get("username")
password = mysql_config.get("password")
db_name = mysql_config.get("db_name")

conn = mysql.connector.connect(
    host=host,
    user=uname,
    password=password,
    database=db_name,
)
cursor = conn.cursor()

def init():
    cursor.execute("CREATE TABLE if not exists guilds (guildID BIGINT(255), prefix VARCHAR(255), welcomeChannelID BIGINT(255), leaveChannelID BIGINT(255))")

def register_guild(guildid, prefix):
    cursor.execute(f"INSERT INTO guilds (guildID, prefix, welcomeChannelID, leaveChannelID) VALUES ({guildid}, '{prefix}', 0, 0)")
    conn.commit()

def get_guild_prefix(guildid):
    cursor.execute(f"SELECT * FROM guilds WHERE guildID = {guildid}")
    data = cursor.fetchone()[1]
    return data

def get_guild_welcomechannel(guildid):
    cursor.execute(f"SELECT * FROM guilds WHERE guildID = {guildid}")
    data = cursor.fetchone()[2]
    if data == 0:
        return None
    else:
        return data

def get_guild_leavechannel(guildid):
    cursor.execute(f"SELECT * FROM guilds WHERE guildID = {guildid}")
    data = cursor.fetchone()[3]
    if data == 0:
        return None
    else:
        return data

def update_guild_prefix(guildid, prefix):
    cursor.execute(f"UPDATE guilds SET prefix = '{prefix}' WHERE guildID = {guildid}")
    conn.commit()
def update_guild_welcome_channel_id(guildid, channelid):
    cursor.execute(f"UPDATE guilds SET welcomeChannelID = {channelid} WHERE guildID = {guildid}")
    conn.commit()
def update_guild_leave_channel_id(guildid, channelid):
    cursor.execute(f"UPDATE guilds SET leaveChannelID = {channelid} WHERE guildID = {guildid}")
    conn.commit()

def remove_guild(guildid):
    cursor.execute(f"DELETE FROM guilds WHERE guildID = {guildid}")
    conn.commit()