import telebot

bot = telebot.TeleBot('6992564836:AAHWId4lFuR0N0iImdIMcJ9VG7RFFdMvjFw')


@bot.meesage_handler(comands=['start'])
def start(message):
    bot.send_message(message.chat.id, text='Бот работает')


bot.polling(none_stop=True)