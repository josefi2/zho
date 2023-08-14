from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="⌯︙مؤقت",
            description=f"⌯︙ ايقاف التشغيل مؤقتا.",
            thumb_url="https://telegra.ph/file/db9e9039ac15449535b05.mp4",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="⌯︙استمرار",
            description=f"⌯︙استمرار التشغيل.",
            thumb_url="https://telegra.ph/file/db9e9039ac15449535b05.mp4",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="⌯︙تخطي",
            description=f"⌯︙تخطي التشغيل الحالي.",
            thumb_url="https://telegra.ph/file/db9e9039ac15449535b05.mp4",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="⌯︙ايقاف",
            description="⌯︙ايقاف التشغيل الحالي.",
            thumb_url="https://telegra.ph/file/db9e9039ac15449535b05.mp4",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="⌯︙تنظيف",
            description="⌯︙تنظيف قوائم التشغيل.",
            thumb_url="https://telegra.ph/file/db9e9039ac15449535b05.mp4",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="⌯︙تكرار",
            description="⌯︙لتكرار التشغيل الحالي.",
            thumb_url="https://telegra.ph/file/db9e9039ac15449535b05.mp4",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
