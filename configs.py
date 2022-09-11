# (c) @AbirHasan2005

import os
import heroku3


class Config(object):
    # Get This From @TeleORG_Bot
    API_ID = int(os.environ.get("9307366"))
    API_HASH = os.environ.get("1ce7a3a4670658d10a01b7e6b090fc07")
    # Get This From @StringSessionGen_Bot
    STRING_SESSION = os.environ.get("1BVtsOKUBuxMy550ZNLT6pUgXzbHmBahK0M-tJ9VpnJHmnpSXnrFj3bemsOZkyoMSthpQxHFCISswqMWgkJF2VuQRKFhC6XtraGUfTrGBTJZ_C9Dg6sHnU6ixoUiQzI6AD2Civ17zYhHNm_R_T0LPNhNtl_8JKwUyzqnMFOok3OpyLV3Kwn4EQsaJDPoS_nGX5XMM5wTrXFTxhgXN77wqOZT7Fv2a1uOhQHc6OO3zAl9rCBSkKYQJHnsupljXLQeaXQ3Me0Q3BRa-snRzSn5NjB-pRlLgQr8OxqKfCP_j7E0OiVQWXcnbfjI8w2jMV6QpU-WycBsUBrd-n0nT0gdzxz6J_JVu4iw=")
    # Forward From Chat ID
    FORWARD_FROM_CHAT_ID = list(set(int(x) for x in os.environ.get("FORWARD_FROM_CHAT_ID", "-775052231").split()))
    # Forward To Chat ID
    FORWARD_TO_CHAT_ID = list(set(int(x) for x in os.environ.get("FORWARD_TO_CHAT_ID", "-798313506").split()))
    # Filters for Forwards
    DEFAULT_FILTERS = "video document photo audio text gif forwarded poll sticker"
    FORWARD_FILTERS = list(set(x for x in os.environ.get("FORWARD_FILTERS", DEFAULT_FILTERS).split()))
    BLOCKED_EXTENSIONS = list(set(x for x in os.environ.get("BLOCKED_EXTENSIONS", "").split()))
    MINIMUM_FILE_SIZE = os.environ.get("MINIMUM_FILE_SIZE", None)
    BLOCK_FILES_WITHOUT_EXTENSIONS = bool(os.environ.get("BLOCK_FILES_WITHOUT_EXTENSIONS", False))
    # Forward as Copy. Value Should be True or False
    FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
    # Sleep Time while Kang
    SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 10))
    # Heroku Management
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    HEROKU_APP = heroku3.from_key(HEROKU_API_KEY).apps()[HEROKU_APP_NAME] if HEROKU_API_KEY and HEROKU_APP_NAME else None
    # Message Texts
    HELP_TEXT = """
This UserBot can forward messages from any Chat to any other Chat also you can kang all messages from one Chat to another Chat.

👨🏻‍💻 **Commands:**
• `!start` - Check UserBot Alive or Not.
• `!help` - Get this Message.
• `!kang` - Start All Messages Kanger.
• `!restart` - Restart Heroku App Dyno Workers.
• `!stop` - Stop Kanger & Restart Service.

©️ **Developer:** @AbirHasan2005
👥 **Support Group:** [【★ʟя★】](https://t.me/JoinOT)"""
