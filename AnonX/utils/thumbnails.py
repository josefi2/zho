import os
import re
import textwrap

import aiofiles
import aiohttp
import numpy as np

from PIL import Image, ImageOps, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from youtubesearchpython.__future__ import VideosSearch

from config import YOUTUBE_IMG_URL
from AnonX import app


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight), Image.LANCZOS)
    return newImage


async def gen_thumb(videoid):
    if os.path.isfile(f"cache/{videoid}.png"):
        return f"cache/{videoid}.png"

    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown Mins"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                views = result["viewCount"]["short"]
            except:
                views = "Unknown Views"
            try:
                channel = result["channel"]["name"]
            except:
                channel = "Unknown Channel"

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(
                        f"cache/thumb{videoid}.png", mode="wb"
                    )
                    await f.write(await resp.read())
                    await f.close()

        youtube = Image.open(f"cache/thumb{videoid}.png")
        image1 = changeImageSize(1280, 720, youtube)
        background = image1.filter(filter=ImageFilter.BoxBlur(30))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.6)
        Xcenter = youtube.width / 2
        Ycenter = youtube.height / 2
        x1 = Xcenter - 250
        y1 = Ycenter - 250
        x2 = Xcenter + 250
        y2 = Ycenter + 250
        logo = youtube.crop((x1, y1, x2, y2))
        logo.thumbnail((520, 520), Image.LANCZOS)
        logo = ImageOps.expand(logo, border=15, fill="white")
        background.paste(logo, (50, 100))
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype("AnonX/assets/font2.ttf", 52)
        font2 = ImageFont.truetype("AnonX/assets/font.ttf", 90)
        arial = ImageFont.truetype("AnonX/assets/font2.ttf", 46)
        name_font = ImageFont.truetype("AnonX/assets/font3.ttf", 40)
        para = textwrap.wrap(title, width=32)
        j = 0
        draw.text(
            (10, 15),
            "بوت هولي ميوزك للمطور جوزيف",
            fill="white",
            stroke_width=1,
            stroke_fill="black",
            font=name_font
        )
        draw.text(
            (1050, 15),
            "جوزيف نمبر 1 بالتلي",
            fill="white",
            stroke_width=1,
            stroke_fill="black",
            font=name_font
        )
        draw.text(
            (1109, 65),
            "لتقلدني تتعب",
            fill="white",
            stroke_width=1,
            stroke_fill="black",
            font=name_font
        )
        draw.text(
            (600, 150),
            "يتم التشغيل الأن",
            fill="white",
            stroke_width=3,
            stroke_fill="black",
            font=font2,
        )
        for line in para:
            if j == 1:
                j += 1
                draw.text(
                    (600, 340),
                    f"{line}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="black",
                    font=font,
                )
            if j == 0:
                j += 1
                draw.text(
                    (600, 280),
                    f"{line}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="black",
                    font=font,
                )

        draw.text(
            (600, 450),
            f"المشاهدات: {views[:23]}",
            fill="white",
            stroke_width=1,
            stroke_fill="black",
            font=arial,
        )
        draw.text(
            (600, 500),
            f"الوقت: {duration[:23]} دقيقة",
            fill="white",
            stroke_width=1,
            stroke_fill="black",
            font=arial,
        )
        draw.text(
            (600, 550),
            f"القناة: {channel}",
            fill="white",
            stroke_width=1,
            stroke_fill="black",
            font=arial,
        )
        try:
            os.remove(f"cache/thumb{videoid}.png")
        except:
            pass
        background.save(f"cache/{videoid}.png", optimize=True, quality=95)
        return f"cache/{videoid}.png"
    except Exception:
        return YOUTUBE_IMG_URL
