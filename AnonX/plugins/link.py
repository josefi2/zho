import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from strings import get_command
from strings.filters import command
from pyrogram.types import Message
from AnonX import app
from strings.filters import command
from strings.filters import command

@app.on_message(
    command(["هولي"])
    & ~filters.edited
)
async def ahmed(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/88187c479e490267db79a.jpg",
        caption=f"""◉ 𝒔𝒐𝒖𝒓𝒄𝒆 𝒉𝒐𝒐𝒍𝒍𝒚 : ❪[𓏺 .ꪀᎥَᥴꫀ ᥕَ᥆𝗋ᥣَძ.🦋. ⟭ཊ ˼](https://t.me/ZHO_JOSEF)❫
◉ Dev : ❪ @JOSEFI0 ❫
◉ 𝙸𝙳      : ❪ 399401433 ❫
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝒔𝒐𝒖𝒓𝒄𝒆 𝒉𝒐𝒐𝒍𝒍𝒚", url=f"https://t.me/JOSEFI0"),
                ],[
                    InlineKeyboardButton(
                        ".ꪀᎥَᥴꫀ ᥕَ᥆𝗋ᥣَძ.🦋.", url=f"https://t.me/ZHO_JOSEF"),
                ],
            ]
        ),
    )
