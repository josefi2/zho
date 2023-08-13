import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "374035"))
API_HASH = getenv("API_HASH", "85f3761ba2d709ff1a5a72cb32c6497b")

BOT_TOKEN = getenv("BOT_TOKEN", "6046893597:AAE3zOhlKW3gferXfWXgc0aH6LSy5HJk4z4")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Cloner:Cloner@cluster0.cgc6t.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001799441743"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "𝐇𝐎𝐋𝐋𝐘 𝐌𝐔𝐒𝐈𝐂 †")

OWNER_ID = list(map(int, getenv("OWNER_ID", "399401433").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", "fe6f162f-935a-4cd9-a360-5f6986366c7e")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "hoollyzhov100")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/JOZANDZHO/HOOLLY.V100")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ZHO_JOSEF")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/JOSEFI0")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180000000000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "18000000000000"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "99999999999999999")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "500"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "500"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "500"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "120"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BAAFtRMASrEmtdAvvQLi3UQg5FccJlWtt6AM_nzNkeKsB3HNBKO3nccmCgYSEvHUzk4Au931nerxzcV2cG6OipPVTNY2dsReEcC9B82XhJhfLBJvT_mymQCURP9ecVJ8sVr1zNCcFTAFD59JQ5iPcxXS3qOCWD-ZGV_JItgnImPxm-eSkAOgOjO8G23Fam6rlAct_i7y1gIDx6ed_mysmCTUw8ywdMsr6HKnHoX0ZdSBNtRJaSuwby1nfBOMAHgSoSzYY9mUzFpUVAryh6EafodZJSd5aJvbB9yjz9R0reXl3lunk7udNdPAi7psjMPRGnjh86vwvtjRmjG8njLhRIAwSToztAAAAAF1CqufAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/88187c479e490267db79a.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/825e7eee6a40bf24c11d7.jpg",
)

PLAYLIST_IMG_URL = "https://telegra.ph/file/079b04c14532d1a3edfb2.jpg"

GLOBAL_IMG_URL = "https://telegra.ph/file/ce27f91b8b5fbf17138c8.jpg"

STATS_IMG_URL = "https://telegra.ph/file/ce27f91b8b5fbf17138c8.jpg"

TELEGRAM_AUDIO_URL = "https://telegra.ph/file/3ae48767f6161412ebf80.jpg"

TELEGRAM_VIDEO_URL = "https://telegra.ph/file/3ae48767f6161412ebf80.jpg"

STREAM_IMG_URL = "https://telegra.ph/file/3ae48767f6161412ebf80.jpg"

SOUNCLOUD_IMG_URL = "https://telegra.ph/file/3ae48767f6161412ebf80.jpg"

YOUTUBE_IMG_URL = "https://telegra.ph/file/3ae48767f6161412ebf80.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/3ae48767f6161412ebf80.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/3ae48767f6161412ebf80.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/3ae48767f6161412ebf80.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://telegra.ph/file/825e7eee6a40bf24c11d7.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://telegra.ph/file/88187c479e490267db79a.jpg"
