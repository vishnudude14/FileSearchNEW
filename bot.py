import logging
import logging.config
import os
import asyncio
from aiohttp import web
from plugins.web_server import web_server  # Ensure this returns a valid web app

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)

from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from database.ia_filterdb import Media
from database.users_chats_db import db
from info import SESSION, API_ID, API_HASH, BOT_TOKEN, LOG_CHANNEL, LOG_STR
from Script import script
from datetime import date, datetime
import pytz
from utils import temp
from typing import Union, Optional, AsyncGenerator
from pyrogram import types

# Get PORT from environment (needed for Koyeb)
PORT = int(os.environ.get("PORT", 8000))  # Use 8000 as default for local testing

class Bot(Client):
    def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        b_users, b_chats = await db.get_banned()
        temp.BANNED_USERS = b_users
        temp.BANNED_CHATS = b_chats
        await super().start()
        await Media.ensure_indexes()
        me = await self.get_me()
        temp.ME = me.id
        temp.U_NAME = me.username
        temp.B_NAME = me.first_name
        self.username = '@' + me.username

        # Start web server
        asyncio.create_task(self.start_web_server())

        logging.info(f"{me.first_name} with Pyrogram v{__version__} (Layer {layer}) started as {me.username}.")
        logging.info(LOG_STR)

        tz = pytz.timezone('Asia/Kolkata')
        today = date.today()
        now = datetime.now(tz)
        time = now.strftime("%H:%M:%S %p")
        await self.send_message(chat_id=LOG_CHANNEL, text=script.RESTART_TXT.format(today, time))       

    async def stop(self, *args):
        await super().stop()
        logging.info("Bot stopped. Bye.")

    async def start_web_server(self):
        """ Starts the web server required for Koyeb deployment """
        app = await web_server()  # Ensure this function returns a valid web app
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, "0.0.0.0", PORT)
        await site.start()
        logging.info(f"Web server started on port {PORT}")

    async def iter_messages(
        self,
        chat_id: Union[int, str],
        limit: int,
        offset: int = 0,
    ) -> Optional[AsyncGenerator["types.Message", None]]:
        """Iterate through a chat sequentially."""
        current = offset
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return
            messages = await self.get_messages(chat_id, list(range(current, current+new_diff+1)))
            for message in messages:
                yield message
                current += 1

app = Bot()
app.run()
