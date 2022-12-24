import json
import telepot
import os
import time
import socket
import Modules.Helper as Helper
import Modules.Commands as Commands
import Modules.BotCommands as BotCommands
import Modules.Settings as Settings

bot_version = '1.0.0'
telebot_path = Helper.GetTelebotPath()
delimiter, prefix = Helper.Get_Prefix_and_Delimiter()
pid = 'Currend PID: ' + str(os.getpid())
HOSTNAME = socket.gethostname()
COMMANDS = Commands.GetInitCommands()

Dirs_Paths = {
    'root': telebot_path,
    'images': f'{telebot_path}{delimiter}Images{delimiter}',
    'documents': f'{telebot_path}{delimiter}Documents{delimiter}',
    'Unauthorized': f'{telebot_path}{delimiter}UnauothorizedUsers{delimiter}',
    'logs': f'{telebot_path}{delimiter}Logs{delimiter}'
}


# dont delete the delimiter....
torrents_path = f'<add_new_torrents_dir_path_here>{delimiter}'


def MessageHandler(msg):
    current_id = msg['from']['id']
    if current_id != settings.ID:
        Helper.Unauthorized(msg=msg, id=current_id, bot=BOT, bot_commands=bot_commands,
                            delimiter=delimiter, path=Dirs_Paths['Unauthorized'])

    else:
        if 'text' in msg:
            command = msg['text']
            global message_id
            message_id = msg['message_id']

            if command == "/help" or command == '/start':
                bot_commands.sendMessage(bot_commands.sendHelp())

            elif command == '/version':
                bot_commands.sendMessage(default_msg)

        elif 'document' in msg:
            filename = msg['document']['file_name']
            file_id = msg['document']['file_id']

            if filename.endswith('.torrent'):
                is_there_a_file = False
                is_path_exists = False

                if torrents_path != "":
                    path = torrents_path + filename
                    if os.path.exists(torrents_path):
                        is_path_exists = True
                        bot_commands.sendMessage(
                            'Recieved torrent file!\nStarting download...')
                else:
                    bot_commands.sendMessage(
                        "Cant accept torrent files because torrents path is empty.")

            elif '.doc' in filename or filename.endswith('.pdf') or '.ppt' in filename:
                path = f'{telebot_path}{delimiter}Documents{delimiter}{filename}'
                is_there_a_file = True
                bot_commands.sendMessage(
                    f'Recieved a document. saving to {path}')

            if not is_there_a_file and is_path_exists:
                bot_commands.saveFile(file_id, path)
            else:
                bot_commands.sendMessage(
                    f'Error getting file: {filename}\nReason: invalid file format')

        elif 'photo' in msg:
            filename = msg['photo']['file_name']
            file_id = msg['photo']['file_id']
            if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
                path = Dirs_Paths['images'] + filename
                bot_commands.saveFile(file_id, path)
            else:
                bot_commands.sendMessage(
                    f'invalid image!\nimage must be a jpg, jpeg or png')


def ReadConfig():
    try:
        with open(f'{telebot_path}{delimiter}settings.json', "r") as f:
            settings = json.loads(f.read())
        return settings
    except Exception as e:
        Helper.WriteToLog(str(e))


def InitSettings(configs):
    if (configs != None):
        id = configs['settings']['ID']
        bot_token = configs['Tokens'][configs['settings']['Current_Bot']]

        return Settings.getSettingsObj(id=id, bot_token=bot_token)
    else:
        Helper.WriteToLog("COULDNT READ CONFIG FILE! ABORTING")
        os._exit(1)


def Main():
    global BOT
    global default_msg
    global settings
    global bot_commands

    try:
        Helper.CreateInitDirs(Dirs_Paths=Dirs_Paths)
        settings = InitSettings(ReadConfig())  # get settings

        BOT = telepot.Bot(settings.BOT_TOKEN)  # init Bot
        BOT.message_loop(MessageHandler)
        bot_commands = BotCommands.GetBotCommandsObj(
            id=settings.ID, bot=BOT, commands=COMMANDS)  # init commands class object
        bot_commands.SelfSetter(id=settings.ID, bot=BOT, commands=COMMANDS)
        bot_commands.PinHelp()

        default_msg = f'{HOSTNAME} is online\npid: {pid}\nBot Ver. {bot_version}'

        bot_commands.sendMessage(default_msg)
    except Exception as e:
        Helper.WriteToLog(str(e))
    while True:
        time.sleep(1)


if __name__ == '__main__':
    Main()
