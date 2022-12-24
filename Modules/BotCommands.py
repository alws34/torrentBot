from datetime import datetime as dt
import json
import os
import requests
import Modules.Helper as Helper


class BotCommands:
    def __init__(self, id, bot, commands):
        self.SelfSetter(id, bot, commands)

    def SelfSetter(self, id, bot, commands):
        self.id = id
        self.bot = bot
        self.commands = commands

    def pinMessage(self, mess_id):
        self.self.bot.pinChatMessage(self.id, mess_id)

    def PinHelp(self):
        try:
            self.self.bot.unpinChatMessage(self.id)
            msg = self.self.bot.sendMessage(self.id, self.sendHelp())
            self.pinMessage(msg['message_self.id'])
        except:
            pass

    def sendMessage(self, message):
        self.bot.sendMessage(self.id, message)

    def sendImage(self, url, caption):
        self.bot.sendPhoto(self.id, url, caption)

    def sendFile(self, path):
        self.bot.sendDocument(path)

    def shellCommand(self, cmd):
        os.system(cmd)

    def saveFile(self, file_id, dest):
        self.bot.download_file(file_id, dest)

    def sendHelp(self):
        try:
            helpmsg = 'Commands list:\n'
            for key, value in self.commands.items():
                helpmsg += f'{key} - {value}\n'
            return helpmsg
        except Exception as e:
            Helper.WriteToLog(str(e))


def GetBotCommandsObj(id, bot, commands):
    return BotCommands(id, bot, commands)
