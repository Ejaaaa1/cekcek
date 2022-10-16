import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5679681575:AAFlcZCEmSF4TgzcbSNO0_kOeP9DteZVWPA")
    AUTH_USERS = int(os.environ.get("AUTH_USERS", "1352705741"))
    SERVER = int("-1001688810274")
