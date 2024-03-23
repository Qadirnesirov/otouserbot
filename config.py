
from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")


API_HASH = getenv("API_HASH", "09e30e6e0b1a4c71e43a055979c51b3b")
API_ID = int(getenv("API_ID", "24066716"))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1002096806763]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "otobotresmi").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID", "otobotblog") or 0)
BOT_VER = "0.1.0@main"
BRANCH = getenv("BRANCH", "main")
CHANNEL = getenv("CHANNEL", "otobotowner")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "mongodb+srv://nesirovq1997:qadir1997@cluster0.pavador.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
GIT_TOKEN = getenv("GIT_TOKEN", "7087723994:AAEdA14WzWwupDIAuSoAeYkPigWvCNDr7rA")
GROUP = getenv("GROUP", "aura_chatt")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
PMPERMIT_PIC = getenv("PMPERMIT_PIC", "https://telegra.ph/file/73064989bd04fcb900ad2.jpg")
REPO_URL = getenv("REPO_URL", "https://github.com/venombolteop/VenomX")
STRING_SESSION1 = getenv("STRING_SESSION1", "AgFvOpwAkqm-9SrYb3Ph_1cDHEm0cCrqU8bU0F8F7yWOr2PI1lulMc_gnE3201tt9t0p-O-1ZsW_AR10dRm7cOklymIGzpv8nnsDZlbjgln6kkrKfRycD-ywZv4CdmybczEImGvO_UXxrtWFQRfFtfQ7Z-JLrUHaksaO4o2fPV9HcuKQE1gQwN7MHgTqSGcZY4rd0NQWu_H9gfU4O81K-xzSzmQGjgQFsVYJpGOci1SHURofEQFnd72iVYOdjY9ZWJhP-HmvJTIslTDzWpkZ5-235Y65z3FUQ5SsL7gyUx84xc3XkH6W6EvMDDU7pSITyKWMG6UUSO_Q2sjURlxKZhJUZGkZOQAAAAFZvEdgAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6184936428").split()))
