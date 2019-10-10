import config
import telebot
from telebot import apihelper

bot = telebot.TeleBot(config.TOKEN)
apihelper.proxy = {'https': 'https://192.53.40.221:8080'}


@bot.message_handler(content_types=['text'])
def get_messages(message):

    output_message = "########################################\n" \
                     "Информация о человеке:\n" \
                     "Имя: " + str(message.from_user.first_name) + "; " + "Никнейм: " + \
                     str(message.from_user.username) + "; " + "ID: " + str(message.from_user.id) + "\n" \
                     "Информация о чате:\n" \
                     "Имя чата: " + str(message.chat.title) + "; " "ID чата: " + str(message.chat.id) + "\n" \
                     "Сообщение: " + str(message.text) + "\n" \
                     "########################################\n"
    bot.send_message(config.my_id, output_message)


bot.polling(none_stop=True, interval=1)
