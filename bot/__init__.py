"""
MIT License

Copyright (c) 2021 Cypher Izumi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os

from pyrogram import Client

API_ID = os.environ.get('API_ID', None)
API_HASH = os.environ.get('API_HASH', None)
TOKEN = os.environ.get('TOKEN', None)


# For Local Deploy:

"""
API_ID = ""
API_HASH = ""
TOKEN = ""
"""

plugins = dict(
    root = "bot/plugins",
)

bot = Client(
    "bot",
    api_id = API_ID,
    api_hash = API_HASH,
    bot_token = TOKEN,
    plugins=plugins
)

print("Starting The Bot Client")

bot.run()

# can be used for getting/sending bot info

info = bot.get_me()

BOT_ID = info.id
BOT_NAME = info.first_name
BOT_USERNAME = info.username
