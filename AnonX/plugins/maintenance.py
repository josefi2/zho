from pyrogram import filters
from pyrogram.types import Message

from strings import get_command, get_string
from AnonX import app
from AnonX.misc import SUDOERS
from AnonX.utils.database import (get_lang, is_maintenance,
                                       maintenance_off,
                                       maintenance_on)
from AnonX.utils.decorators.language import language
from strings.filters import command

# Commands
MAINTENANCE_COMMAND = get_command("MAINTENANCE_COMMAND")


@app.on_message(filters.command(MAINTENANCE_COMMAND) & SUDOERS)
@app.on_message(command(["الصيانه"]) & SUDOERS)
async def maintenance(client, message: Message):
    try:
        language = await get_lang(message.chat.id)
        _ = get_string(language)
    except:
        _ = get_string("en")
    usage = _["maint_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    message.chat.id
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "تفعيل":
        if await is_maintenance() is False:
            await message.reply_text(
                "⌯︙تم تفعيل وضع الصيانه."
            )
        else:
            await maintenance_on()
            await message.reply_text(_["maint_2"])
    elif state == "تعطيل":
        if await is_maintenance() is False:
            await maintenance_off()
            await message.reply_text(_["maint_3"])
        else:
            await message.reply_text(
                "⌯︙ما اذكر انت فعلت وضع الصيانه."
            )
    else:
        await message.reply_text(usage)
