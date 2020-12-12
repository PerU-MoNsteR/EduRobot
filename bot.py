import logging

from config import API_HASH, API_ID, TOKEN, disabled_plugins, log_chat
from pyrogram import Client, idle
from pyrogram.errors.exceptions.bad_request_400 import BadRequest

with open("version.txt") as f:
    version = f.read().strip()


client = Client(
    "bot",
    API_ID,
    API_HASH,
    bot_token=TOKEN,
    workers=24,
    plugins=dict(root="plugins", exclude=disabled_plugins),
)

with client:
    if __name__ == "__main__":
        client.me = client.get_me()
        try:
            client.send_message(
                log_chat, "**Bot started**\n\n" f"**Version:** {version}"
            )
        except BadRequest:
            logging.warning("Unable to send message to log_chat.")
        idle()
