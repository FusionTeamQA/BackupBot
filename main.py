import telebot
from telebot import types

bot = telebot.TeleBot('5801609804:AAHrCTS4ZDHDiTDibTvey6Q8KeFC5-Tt3es')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == "Привет":
#         bot.send_message(message.chat.id, "И тебе привет", parse_mode='html')
#     elif message.text == "id":
#         bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
#     elif message.text == "photo":
#         photo = open('icon.png', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, "Не понимаю тебя", parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Агонь фото')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://fusion-tech.pro/"))
    bot.send_message(message.chat.id, 'Перейдите на сайт и посмотри на это великолепие', reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('Веб сайт')
    start = types.KeyboardButton('Старт')

    markup.add(website, start)
    bot.send_message(message.chat.id, 'Перейдите на сайт и посмотри на это великолепие', reply_markup=markup)


bot.polling(none_stop=True)
