import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

#          
                
@app.on_message(
    command(["المطور","جوزيف","مطور السورس","مبرمج السورس"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/d2bb88248fb52b9944b02.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[𓏺 𓆩␥⬳᩺𝕁𝕆𝕊𝔼𝔽𑑛𓆪 ˼](https://t.me/JOSEFI0)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @JOSEFI0 ❫
◉ 𝙸𝙳      : ❪ 399401433 ❫
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓆩␥⬳᩺𝕁𝕆𝕊𝔼𝔽𑑛𓆪", url=f"https://t.me/JOSEFI0"), 
                 ],[
                   InlineKeyboardButton(
                        "⌞ 𝒔𝒐𝒖𝒓𝒄𝒆 𝒉𝒐𝒐𝒍𝒍𝒚 ⌝", url=f"https://t.me/ZHO_JOSEF"),
                ],

            ]

        ),

    )
