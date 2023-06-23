import mysql.connector

host = "dabu.cz"
uname = "u24_WxwevBoD9e"
password = "=Wmba!H=k+Y97wBha4lFm@qH"
db_name = "s24_test"

db = mysql.connector.connect(
    host=host,
    user=uname,
    password=password,
    database=db_name
)
cursor = db.cursor()

def init():
    cursor.execute("CREATE TABLE if not exists guilds (guildID BIGINT(255), prefix VARCHAR(255), welcomeChannelID BIGINT(255), leaveChannelID BIGINT(255))")

def register_guild(guildid, prefix):
    cursor.execute(f"INSERT INTO guilds (guildID, prefix, welcomeChannelID, leaveChannelID) VALUES ({guildid}, '{prefix}', 0, 0)")
    db.commit()

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
    db.commit()
def update_guild_welcome_channel_id(guildid, channelid):
    cursor.execute(f"UPDATE guilds SET welcomeChannelID = {channelid} WHERE guildID = {guildid}")
    db.commit()
def update_guild_leave_channel_id(guildid, channelid):
    cursor.execute(f"UPDATE guilds SET leaveChannelID = {channelid} WHERE guildID = {guildid}")
    db.commit()

def remove_guild(guildid):
    cursor.execute(f"DELETE FROM guilds WHERE guildID = {guildid}")
    db.commit()