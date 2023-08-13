import asyncio
from pyrogram import Client, filters
from AnonX import app
import random
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

####  


iddof = []
@app.on_message(
    command(["تعطيل ايدي هولي"])
    & filters.group
    & ~filters.edited
)
async def iddlock(client, message):
   get = await app.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in ["creator", "administrator"]:
      if message.chat.id in iddof:
        return await message.reply_text("تم معطل من قبل🔒")
      iddof.append(message.chat.id)
      return await message.reply_text("تم تعطيل الايدي بنجاح ✅🔒")
   else:
      return await message.reply_text("**اذا مو ادمن لضل تبعبص بالبوت**")

@app.on_message(
    command(["تفعيل ايدي هولي"])
    & filters.group
    & ~filters.edited
)
async def iddopen(client, message):
   get = await app.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in ["creator", "administrator"]:
      if not message.chat.id in iddof:
        return await message.reply_text("الايدي مفعل من قبل ✅")
      iddof.remove(message.chat.id)
      return await message.reply_text("تم فتح الايدي بنجاح ✅🔓")
   else:
      return await message.reply_text("** اذا مو ادمن لضل تبعبص بالبوت **")




@app.on_message(
    command(["id"])
    & filters.group
    & ~filters.edited
)
async def iddd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f""" ↬ ¦آسمڪ :『{message.from_user.mention}』\n ↬ ¦يوزرڪ :『@{message.from_user.username}』\n ↬ ¦آيديڪ : 『`{message.from_user.id}`』 \n ↬ ¦البايو : 『`{usr.bio}`』 \n ↬ ¦المجموعه : 『`{message.chat.title}`』 \n ↬ ¦ايدي المجموعه : 『`{message.chat.id}`』""", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ 𝒔𝒐𝒖𝒓𝒄𝒆 𝒉𝒐𝒐𝒍𝒍𝒚 ›", url=f"https://t.me/JOSEFI0")
                ],
            ]
        ),
    )



iddof = []
@app.on_message(
    command(["قفل صورتي","تعطيل صورتي"])
    & filters.group
    & ~filters.edited
)
async def lllock(client, message):
   get = await app.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in ["creator", "administrator"]:
      if message.chat.id in iddof:
        return await message.reply_text("صورتي معطل من قبل✅")
      iddof.append(message.chat.id)
      return await message.reply_text(" تم تعطيل صورتي بنجاح✅🔒")
   else:
      return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")

@app.on_message(
    command(["فتح صورتي","تفعيل صورتي"])
    & filters.group
    & ~filters.edited
)
async def idljjopen(client, message):
   get = await app.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in ["creator", "administrator"]:
      if not message.chat.id in iddof:
        return await message.reply_text("صورتي مفعل من قبل✅")
      iddof.remove(message.chat.id)
      return await message.reply_text("تم فتح صورتي بنجاح ✅🔓")
   else:
      return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")




@app.on_message(
    command(["صورتي"])
    & filters.group
    & ~filters.edited
)
async def idjjdd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    i = ["0","10", "15","20", "25","30","35", "40","45", "50","55", "60"," 66", "70","77", "80","85", "90","99", "100","1000" ]
    ik = random.choice(i)
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**نسبة جمالك يالحب** \n│ \n : {ik} %😂❤️", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ 𝒔𝒐𝒖𝒓𝒄𝒆 𝒉𝒐𝒐𝒍𝒍𝒚 ›", url=f"https://t.me/JOSEFI0")
                ],
            ]
        ),
    )
