class Settings:
    def __init__(self, id, bot_token):
        self.SetSettings(id, bot_token)

    def SetSettings(self, id,  bot_token):
        self.ID = id
        self.BOT_TOKEN = bot_token


def getSettingsObj(id, bot_token):
    return Settings(id, bot_token)
