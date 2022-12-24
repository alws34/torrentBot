from os import name as os_name, path as os_path, getcwd, makedirs
from datetime import datetime as dt


def Get_Date_Time():
    return dt.now()


def GetDateTimeStringify(format="%d_%m_%Y"):
    return Get_Date_Time().strftime(format)


def GetTelebotPath():
    # if os_name == 'nt':
    telebot_path = getcwd()  # + '\\Telebot'
    return telebot_path


def WriteToLog(msg):
    delimiter, prefix = Get_Prefix_and_Delimiter()
    log_path = f'{GetTelebotPath()}{delimiter}Logs{delimiter}{GetDateTimeStringify()}.log'
    mode = 'a'
    if not os_path.exists(log_path):
        mode = 'w+'

    with open(log_path, mode, encoding='utf-8') as log_file:
        log_file.write(
            f'{GetDateTimeStringify(format="%H:%M:%S")}::\t\t{msg}\n\n')


def CommandNotFound(cmd, commands, bot_commands):
    try:
        if cmd[0] not in commands and cmd[0] != '/start':
            bot_commands.sendMessage(
                "Command not found\nPlease try one of the following:")
            bot_commands.sendMessage(bot_commands.sendHelp())
    except Exception as e:
        WriteToLog(str(e))


def Unauthorized(msg, id, bot, bot_commands, delimiter, path):
    try:
        WriteToLog('UNAUTORIZED ACCESS ALERT:\n' + str(msg['from']))
        with open(path + delimiter + str(id) + '.txt', 'w+') as f:
            f.write('FROM:\n' + str(msg['from']) +
                    '\nCHAT:\n' + str(msg['chat']))
        bot.sendMessage(id, 'Unauthorized USER!\n')
        bot_commands.sendMessage('Unautorized Access Attempt from:\n' +
                                 str(msg['from']))
    except Exception as e:
        WriteToLog(str(e))


def CreateInitDirs(Dirs_Paths):
    for i in Dirs_Paths.items():
        CreateFolders(i[1])


def Get_Prefix_and_Delimiter():
    if os_name == 'nt':
        delimiter = '\\'
    elif os_name == 'posix':
        delimiter = '/'
    prefix = f'{getcwd()}{delimiter}'

    return delimiter, prefix


def CreateFolders(path):
    if not os_path.exists(path):
        makedirs(path)
