import os

class Config(object):

    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("BOT_TOKEN")

    # The Telegram API things
    # Get these values from my.telegram.org
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    # Channel Username
    CHANNEL_USERNAME = os.environ.get("CHANNEL_USERNAME")
    # Your Group Username
    GROUP_USERNAME = os.environ.get("GROUP_USERNAME")
    # Owner ID
    OWNER_USERNAME =os.environ.get("OWNER_USERNAME")
    # OWNER NAME
    OWNER_NAME =os.environ.get("OWNER_NAME")
