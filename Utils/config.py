import json
with open("config.json") as f:
    config = json.load(f)

mysql_config = config["mysql"]
host = mysql_config.get("host")
uname = mysql_config.get("username")
password = mysql_config.get("password")
db_name = mysql_config.get("db_name")

TOKEN = config.get("token")
STATUS = config.get("status")
FOOTER = config.get("footer")
ICON = config.get('icon_url')
default_prefix = config.get('default_prefix')