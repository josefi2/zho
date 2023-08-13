from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from AnonX import app
from AnonX.core.call import Anon
from AnonX.utils.database import set_loop
from AnonX.utils.decorators import AdminRightsCheck, AdminRightsCheckCB
from AnonX.utils.inline.play import close_keyboard
from strings.filters import command
# Commands
STOP_COMMAND = get_command("STOP_COMMAND")
STOP_COMMAND_chh = get_command("STOP_COMMAND_chh")
import requests

async def check_subscription(user_id):
    channel_username = "ZHO_JOSEF"  # معرف القناة الفعلي

    bot_token = "6046893597:AAE3zOhlKW3gferXfWXgc0aH6LSy5HJk4z4"  # رمز معرف البوت الخاص بك
    api_url = f"https://api.telegram.org/bot{bot_token}/getChatMember?chat_id=@{channel_username}&user_id={user_id}"
    
    response = requests.get(api_url)
    data = response.json()

    if response.status_code == 200 and data["ok"]:
        status = data["result"]["status"]
        if status == "left":
            return False
        else:
            return True

    return False

@app.on_message(
    filters.command(STOP_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@app.on_message(
    command(["ايقاف", f"كافي"])
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    user_id = message.from_user.id

    # التحقق من اشتراك المتخدم في القناة
    is_subscribed = await check_subscription(user_id)
    if not is_subscribed:
        channel_name = "ꪀᎥَᥴꫀ ᥕَ᥆𝗋ᥣَძ.🦋"
        channel_url = "https://t.me/ZHO_JOSEF"
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton(channel_name, url=channel_url)]]
        )
        return await message.reply_text(
            "⚠️︙عذراً، عليك الانضمام الى قناة البوت أولاً :",
            reply_markup=keyboard
        )

    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await Anon.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_9"].format(message.from_user.first_name),
        reply_markup=close_keyboard,
    )
@app.on_message(
    command(STOP_COMMAND_chh)
    & filters.channel
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheckCB
async def stop_music_ch(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await Anon.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    if message.sender_chat:
        mention = f'<a href=tg://user?id={message.chat.id}>{message.chat.title}</a>'
    else:
        mention = message.from_user.mention
    await message.reply_text(
        _["admin_9"].format(mention)
    )
