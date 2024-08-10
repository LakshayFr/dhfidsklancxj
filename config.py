import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("24073111"))
API_HASH = getenv("9775a27670d26923630d4a86528fc8db")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7338308938:AAHELveVEN5SUqhTchln_0H6wVu-9vKfhrQ")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://hypercheckerop:cqfSwfrQfvW0SElC@cluster0.uqlfs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-4233455547", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("6574060333", 1356469075))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AnonymousX1025/AnonXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/hypermpshop")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/hyperdiscussion")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("31c7b6da5759489992cfa776d46eeeee", None)
SPOTIFY_CLIENT_SECRET = getenv("efc0bbd704564f4f865f080f2d621182", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("BQFvU5cAclGmgHdIEDmyA-oyFXqGZzIqCPuOvQ3FtCbed5Uc5S5H58zJuLrWYUWxCi4A4HUU103rlGbxqfpsRCjZJrJiBamNOk18vfRpsuCZO8ebhvJxLsgQX7kfv0c3j-f-F_2joDk27h9ERpQilSMSAgdWnJK0R8wI62yfAb_HdQonXnDQR8G6IpA0Xr9DKq5Q1mgwpUXc6VE5QDZJ7QnXQg9CkTKRslCmgOvmEmr_0GC8rBybXFVNVa1yN7iD7uZ-sngxP8IJNV-iRQ5xNlU1xB4SETtJP_acDgUlKAqcUrM2z0ghbBoP0tzsT07kD0Mauc8NmDzoDkrgi5Y0y6nEC_MfBAAAAAF3TKu9AA", None)
STRING2 = getenv("BQFvU5cAQKZPgSONI2IsDnxRQXyEQZGpDNv7b0hF8bsvvjY3b7ds4zTe2FHAWg0zus7j37L2fBOu7MHtk7ifnbPvocExZb41WjtKQ25A1XMzh-UkgPrgy0Lt7bZ689G7_kG9Dqbiks2or_se1oQrIoZ8gS6HrxxyOfWKJpe14ytPfdyCq9A9GU53YkDQOSYHrzUbGQwq33NDdae2qPoNCAL1RTxyrIIfjJ8VVNVSeh-I0DS6O6LWremoZz-30G10tD2m4ONSqw7gMbSngdzl9c3aT2DfkNDHgJ2uVFsyANYvZuMdUpM9nrbMDZxGkHLg2IiFIW7fzQ5uxjF6Po7sdU_dyHwwAAAAF3TKu9AA", None)
STRING3 = getenv("BQFvU5cASERQUTtL_R0eIHCr0hj7zAW-Jljgq7QXUQTq4-WLOSCThMP9U2X8xFRLV8Oy9-Wn2blVtygGn358Byg4KjOF234T4QAS4yPiY1QJsnVrsuvRE4d-DRwIYUL-LutkXxT8kC5nEbLzeQGwL8h4KNIHK-tO6jbBHiitbju9gcSKS00t1sRi9KkwmL2DePU4iuo5n4X2Mwq6z4HgQBKD5WhmwZOHFnxvfWCVLqtIOUz4vXqmgT34JRCJ-RFU2ecUn_pbvn8aBS0Y0NGiCVVknPc_TKQMrYvAIxoDN5MDCWWG-KyjRFZvTlM8MbaiA-gguCklfkQZyCVZ6YBw0sv7510wAAAAF3TKu9AA", None)
STRING4 = getenv("BQFvU5cAfUUQMxNJvJew2sepO9X3ZCKjPyLZVw5g_PxJ1AqhHzTZmuaPAJnzTa1ziEXcqbl9DX3kV5GsSp_MEmdCx3sMVdYxQxhepgSWgJe0HfVSgUs2Z4aOtPclkwkCxTIW4X6AZIBI9GXcReSNpJzdO-6-Bm0wClKv1ljXWAD34qCBOSLN5h9hr6m1GAv9KRaNQkWBwC9MtQDXGJ9YpeYy3vM5km8U0zubYprynD2QZkYCDyHTMCob7LmRxnPDjh5aB3SL9DKS4eL1izk6BE0f9x51vqrCqckca91HSnd6sWWKmQi7kC_Vr-T7uUjr9uPeQ4qB47WwL0zZqfwf3uG8ZrIkWwAAAAF3TKu9AA", None)
STRING5 = getenv("BQFvU5cAJSjck5uIY2I8mLM1KBZ-TViWmIQsG9eAIon6sG3nSkMNyVXJNgEoRl8_lRAdduteCRgSB_SPeT0-bxYlfwFLiLelQSTXkrx0usI7JD7aKptDZiOWbk5RKn8QtZF_-UxqE3EgmlZltbyG3ayNZWUV00m1eXPq8hlaI-OphbjQ3A_XKcWty0WsfM1_QG3V98TL1aZtzFREY2-IfKhjQFrL6LgNzbwY3NuXfDXn-9EvNKmDYg1f4HpO6PxISXQn5t8czARcyhgYbI_aggT0OinyHB0v9ZqBrpGx9cu5MUZj_ijQwbQ0cQS2a9N5NOX_KI48uUiYZrJVhjbaC8ERtlhwAAAAF3TKu9AA", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/25efe6aa029c6baea73ea.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/b8a0c1a00db3e57522b53.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
