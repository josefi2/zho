from pyrogram import filters
from strings.filters import command

import config
from strings import get_command
from AnonX import app
from AnonX.misc import SUDOERS
from AnonX.utils.database import autoend_off, autoend_on
from AnonX.utils.decorators.language import language

# Commands
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
@app.on_message(command(["انهاء تلقائي"]) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "**⌯︙استعمل:**\n\n/autoend [تفعيل|تعطيل]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "تفعيل":
        await autoend_on()
        await message.reply_text(
            "⌯︙ تم تفعيل الانهاء التلقائي."
        )
    elif state == "تعطيل":
        await autoend_off()
        await message.reply_text("⌯︙ تم تعطيل الانهاء التلقائي.")
    else:
        await message.reply_text(usage)
