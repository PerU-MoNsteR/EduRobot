from datetime import datetime

from config import prefix
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("ping", prefix))
async def ping(c: Client, m: Message):
    first = datetime.now()
    sent = await m.reply_text("**Pong!**")
    second = datetime.now()
    await sent.edit_text(f"**Pong!** `{(second - first).microseconds / 1000}`ms")
