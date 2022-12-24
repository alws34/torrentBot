# torrentBot
This Telegram bot will download .torrent files sent to it and add them to a specific directory for the torrent client to auto download

* this is a module from another-bigger bot frankenstined to work as a standalone telegram bot. 
for any problem, please open an issue. 

installation instructions: 

[install python on your computer](https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe)

[install the the "telepot" library](https://telepot.readthedocs.io/en/latest/#installation)

[Create a telegram bot using botfather](https://blog.devgenius.io/how-to-set-up-your-telegram-bot-using-botfather-fd1896d68c02)
 * place the bot token (recieved from botfather) in the settings.json file at the designated location 
 * place your chat id in the settings.json file at the designated location -- (get chat id)[https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id]  -- this is for making the bot respond only to you 
 (the response by Yigit Yuksel seems the easiest... there are also bots on thelgram that can do this... search for "@iDCHATBOT" or "@chatid_echo_bot"....)

run this script at startup (for linux users -run this as a serive) 
for windows users, run it using "task scheduler" using <strong>pythonw.exe</strong> instead of python.exe
(https://stackoverflow.com/questions/9705982/pythonw-exe-or-python-exe)

[creating a task using task scheduler](https://www.ibm.com/docs/en/datacap/9.1.6?topic=application-configuring-windows-task-scheduler-automatically-run-ruleset)





* I take no responsibilty on any damage caused to you by using this code. 

