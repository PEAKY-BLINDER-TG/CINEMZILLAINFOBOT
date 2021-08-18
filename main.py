import os
from pyrogram import Client, filters
from pyrogram.types import *
from config import Config

Telegram = Client(
    "Telegram Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

# Translation = Commands

@Telegram.on_message(filters.command(["start"]))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = START_BUTTON
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Telegram.on_message(filters.command(["help"]))
async def help(bot, update):
    text = HELP_TEXT
    reply_markup = HELP_BUTTON
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Telegram.on_message(filters.command(["about"]))
async def about(bot, update):
    text = ABOUT_TEXT
    reply_markup = ABOUT_BUTTON
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Telegram.on_message(filters.command(["channel"]))
async def channel(bot, update):
    text = CHANNEL_TEXT
    reply_markup = CHANNEL_BUTTON
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Telegram.on_message(filters.command(["group"]))
async def group(bot, update):
    text = GROUP_TEXT
    reply_markup = GROUP_BUTTON
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Telegram.on_message(filters.command(["developer"]))
async def developer(bot, update):
    text = DEVELOPER_TEXT
    reply_markup = DEVELOPER_BUTTON
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Telegram.on_message(filters.command(["source"]))
async def source(bot, update):
    text = SOURCE_TEXT
    reply_markup = SOURCE_BUTTON
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

# Translation = CALLBACK_DATA

@Telegram.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=START_BUTTON,
            disable_web_page_preview=True
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTON,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTON,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()

# Translation = TEXT

START_TEXT = """HAI {}, 

AM A BOT OF @CINEMAZILLA GROUP I WOULD STORE ALL DETAILS ABOUT THEIR TEAM. 
FOR MORE CHECK THE BUTTONS BELOW
"""

HELP_TEXT = """**--🛠 HELP--**

**➠ Telegram Bot**

**➠ Easy Bot**

**Available Commands 🔻**

☆ /start - To Restart Me
☆ /help - For More Help
☆ /about - More About Me
☆ /channel - MY Channel
☆ /group - MYGroup
☆ /developer - MY Developer
☆ /source - MY Source Code

👲 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : [ʙx ʙᴏᴛᴢ](https://t.me/BX_Botz) 
"""

ABOUT_TEXT = """
*NOTHING IS GREAT AND NOTHING IS MORE IMPORTANT ABOUT ME*

AM A BOT TO STORE ONLY INFOS AND DATA'S ABOUT @CINEMAZILLA 
"""

CHANNEL_TEXT = """**OUR CHANNELS**
"""

GROUP_TEXT = """**OUR GROUP**
"""

DEVELOPER_TEXT = """**WANT TO ADD ANYTHING**
"""

SOURCE_TEXT = """**FOR NEW MOVIES UPDATE CHECK **
"""

# Translation = BUTTONS

START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🛠️Help', callback_data="help")
        ],
    [
        InlineKeyboardButton('🔰About', callback_data="about"),
        InlineKeyboardButton('Close 🔒', callback_data="close")     
        ]]
    )

HELP_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏠Home', callback_data="home"),
        InlineKeyboardButton('🔰About', callback_data="about"),
        InlineKeyboardButton('Close 🔒', callback_data="close")
        ]]
    )

ABOUT_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏠Home', callback_data="home"),
        InlineKeyboardButton('🛠️Help', callback_data="help"),
        InlineKeyboardButton('Close 🔒', callback_data="close")
        ]]
    )

CHANNEL_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🎁 Channel', url=f"https://telegram.me/{Config.CHANNEL_USERNAME}")
        ]]
    )

GROUP_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('👥 Group', url=f"https://telegram.me/{Config.CHANNEL_USERNAME}")
        ]]
    )

DEVELOPER_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🧑‍💻 Developer', url=f"https://telegram.me/{Config.OWNER_USERNAME}")
        ]]
    )

SOURCE_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🎨 Source Code', url="https://GitHub.Com/BXBotz/Telegram-Bot")
        ]]
    )   

Telegram.run()
