import asyncio
import os
import time
import requests
import shlex
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from asyncio import gather
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



@app.on_message(command(["تلغراف", "00", "ميديا"]) & ~filters.edited)
async def telegraph(client: Client, message: Message):
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
    replied = message.reply_to_message
    if not replied:
        await message.reply("🤕 ¦ الرد على ملف وسائط مدعوم\n• حط صوره و اكتب عليها 00")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4"),
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply("غير مدعوم!!")
        return
    download_location = await client.download_media(
        message=message.reply_to_message,
        file_name="root/downloads/",
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        await message.reply(
            f"<b>• الــرابـط:-</b>\n\n <code>https://telegra.ph{response[0]}</code>",
            quote=True,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🎯 ¦ افـتح الـرابـط", url=f"https://telegra.ph{response[0]}"),
                    InlineKeyboardButton(text="♻️ ¦ مشـاركه الـرابـط", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}"),
                    InlineKeyboardButton(text="‹ 𓆩␥⬳᩺𝕁𝕆𝕊𝔼𝔽𑑛𓆪 ›", url=f"https://t.me/JOSEFI0")
                ],
            ]
        )
    )
    finally:
        os.remove(download_location)





@app.on_message(command(["معلوماته", "كشف"]) & filters.group & ~filters.edited) 
async def hshs(client: Client, message: Message):
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
    usr = await client.get_users(message.reply_to_message.from_user.id)
    name = usr.first_name#
    user_id = message.reply_to_message.from_user.id#
    chat_idd = message.chat.id#
    chat_username = f"@{message.chat.username}" #
    chat_name = message.chat.title#
    username = f"@{message.reply_to_message.from_user.username}"#
    async for photo in client.iter_profile_photos(message.reply_to_message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""**[⌞ 𝒔𝒐𝒖𝒓𝒄𝒆 𝒉𝒐𝒐𝒍𝒍𝒚 ˼⁩](https://t.me/JOSEFI0)\n\n🐉 ¦ ɴᴀᴍᴇ : {name}\n🤡 ¦ ᴜѕᴇ : {username}\n🔥 ¦ ɪᴅ : `{user_id}`\n🔅 ¦ ɪᴅ ᴄʜᴀᴛ : `{chat_idd}`\n💭 ¦ ᴄʜᴀᴛ : {chat_name}\n🐊 ¦ ɢʀᴏᴜᴘ : {chat_username} \n**""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ 𓆩␥⬳᩺𝕁𝕆𝕊𝔼𝔽𑑛𓆪 ›", url=f"https://t.me/JOSEFI0"),
                ],
            ]
        ),
    )     



@app.on_message(
    command(["بايو","البايو"])
    & filters.group
    & ~filters.edited
)
async def biio(client, message):
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
    nq = await client.get_chat(message.from_user.id)
    bio = nq.bio
    await message.reply_text(bio
  )
@app.on_message(
    command(["شخصيتي", "معلوماتي", "شخصيه"])
    & filters.group
    & ~filters.edited
)
async def ppdi(client: Client, message: Message):
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
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""**• انـت »   {message.from_user.mention()} فلق طرك مو بشر حلغوم🔥😮‍💨**""", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                         "‹ 𓆩␥⬳᩺𝕁𝕆𝕊𝔼𝔽𑑛𓆪 ›", url=f"https://t.me/JOSEFI0")
                ],
            ]
        ),
    )
 
 
 
 
@app.on_message(command(["تحويل صوره", "تحويل الصوره"]))
async def sticker_image(client: Client, message: Message):
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
    reply = message.reply_to_message
    if not reply:
        return await message.reply("الرد على ملصق.")
    if not reply.sticker:
        return await message.reply("الرد على ملصق.")
    m = await message.reply("يتم المعالجه..")
    f = await reply.download(f"{reply.sticker.file_unique_id}.png")
    await gather(*[message.reply_photo(f),message.reply_document(f)])
    await m.delete()
    os.remove(f)



@app.on_message(command(["الكروب", "كروب"]) & filters.group & ~filters.edited)
async def ginnj(client: Client, message: Message):
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
    chat_idd = message.chat.id
    chat_name = message.chat.title
    chat_username = f"@{message.chat.username}"
    photo = await client.download_media(message.chat.photo.big_file_id)
    await message.reply_photo(photo=photo, caption=f"""**🐲 ¦ الاسم » {chat_name}\n🚸 ¦ ايدي الكروب »  -{chat_idd}\n🐊 ¦ رابط » {chat_username}**""",     
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ 𓆩␥⬳᩺𝕁𝕆𝕊𝔼𝔽𑑛𓆪 ›", url=f"https://t.me/JOSEFI0")
                ],
            ]
        ),
    )
    
