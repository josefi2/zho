import asyncio
from pyrogram import Client, filters
from AnonX import app
from strings import get_command
from strings.filters import command
from AnonX.utils.database import *
from pyrogram.types import Message, VoiceChatStarted, VoiceChatEnded
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError,AlreadyJoinedError)
from AnonX.core.call import Anon
from AnonX.utils.database import get_assistant
from strings.filters import command

@app.on_message(filters.voice_chat_started)
async def stcall(client: Client, message: Message): 
      Startt = "تم بدأ محادثه صوتيه"
      await message.reply_text(Startt)

@app.on_message(filters.voice_chat_ended)
async def encall(client: Client, message: Message): 
      Enddd = "تم إغلاق المحادثه الصوتيه"
      await message.reply_text(Enddd)

@app.on_message(filters.voice_chat_members_invited)
async def zoharyy(client: Client, message: Message): 
           text = f"- قام {message.from_user.mention}\n - بدعوة : "
           x = 0
           for user in message.voice_chat_members_invited.users:
             try:
               text += f"[{user.first_name}](tg://user?id={user.id}) "
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text} ")
           except:
             pass
