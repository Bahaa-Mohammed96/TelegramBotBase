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

from bot import dispatcher, updater

from telegram import Update
from telegram.ext import CallbackContext, run_async, 


# Using send_message method

def start(update: Update, context: CallbackContext):
    if update.effective_chat.type != "private": #Ensuring that bot only replies to PMs
        pass
    else: 
        context.bot.send_message(chat_id=update.effective_chat.id, text="Hello There!, Join My Support Group! @TangentChats")


START_HANDLER = CommadHandler("start", start, run_async=True)

dispatcher.add_handler(START_HANDLER)
# Copyright (c) 2021

if __name__ == "__main__":
    print("Starting The Bot Client")
    updater.start_polling()