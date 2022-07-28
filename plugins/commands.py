from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from variables import DELAY, PICS
import os 

@Client.on_message(filters.private & filters.command(["start"]))
async def start_message(client, msg):
    await message.reply_chat_action("Typing")
    await asyncio.sleep(DELAY)
    await message.reply_photo(
       photo=random.choice(PICS),
       caption=f"**Sorry bro,You didn't Joined Our Updates Channel Join now and start again🙏**",
       reply_markup=InlineKeyboardMarkup(
       [
           [
               InlineKeyboardButton(text="open link", url=f"https://telegra.ph{response[0]}"),
               InlineKeyboardButton(text="share link", url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}")
           ],
           [InlineKeyboardButton(text="✗ Close ✗", callback_data="close")]
       ]
    )
 )
