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


from pyrogram import filters 
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from bot import bot

btns = [
    [
        InlineKeyboardButton(
            text="Join My Support!", url="https://telegram.dog/TangentChats"
        ),
    ]
]

# A method using send_message 
# Usage: /start
@bot.on_message(filters.command("start") & filters.private) # Ensuring that Bot only replies to commands in its PM
async def start(_, message):
    await bot.send_message(message.chat.id, 
    "Thanks for using me! \nJoin My Support Chat!", 
    reply_markup=InlineKeyboardMarkup(btns),
    disable_web_page_preview=True
    )

# A method using reply_text and reply_photo methods
# Usage: /hello
@bot.on_message(filters.command("hello") & filters.private) # Ensuring that Bot only replies to commands in its PM
async def hello(_, message):
    PHOTO = "https://telegra.ph/file/ed42f17396b2546801df6.jpg"
    await message.reply_photo(PHOTO, text="This was sent using reply_photo attribute!")
    await message.reply_text("This was sent using reply_text attribute!")
