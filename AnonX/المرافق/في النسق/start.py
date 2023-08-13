from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=". اضفني الى مجموعتك .",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="مساعده",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="الاعدادات", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=".اضفني الى مجموعتك . ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="- المساعده .", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="- الدعم .", user_id=OWNER
            ),
            InlineKeyboardButton(
                text="- BoT OWNER .", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="- Dev Source .", user_id=OWNER
            )
        ],
     ]
    return buttons
