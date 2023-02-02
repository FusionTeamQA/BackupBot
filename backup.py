# -*- coding: utf-8 -*-
import telebot
from telebot import types
import setting
import psycopg2
import logging
import os, sys
from requests.exceptions import ConnectionError, ReadTimeout
from setting import db_host, db_user, db_password, db_name

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
bot = telebot.TeleBot(setting.token)

user_dict = {}
user_chats = 0


class User:

    def __init__(self, name):
        self.name = None
        self.age = None
        self.nums = None
        self.location = None
        self.experience = None
        self.format_work = None

        keys = ['name', 'age', 'nums', 'location', 'experience', 'format_work']
        for key in keys:
            self.key = None


@bot.message_handler(commands=['start'])  # стартовая команда
def start(message):
    conn = psycopg2.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
        id INTEGER, 
        user_first_name TEXT, 
        user_last_name TEXT, 
        username TEXT
        )''')
    conn.commit()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
        id INTEGER, 
        user_first_name TEXT, 
        user_last_name TEXT, 
        username TEXT
        )''')
    conn.commit()

    people_id = message.from_user.id
    cursor.execute(f"SELECT id FROM users WHERE id = {people_id}")
    data = cursor.fetchone()
    if data is None:
        USER_ID = [message.from_user.id, message.from_user.first_name, message.from_user.last_name,
                   message.from_user.username]
        cursor.execute("INSERT INTO users VALUES(?,?,?,?);", USER_ID)
        conn.commit()
    else:
        print("Старт бота - Такой пользователь уже есть в базе данных")
        print(message.from_user.username)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇷🇺 Русский")
    btn2 = types.KeyboardButton('🇬🇧 English')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)


@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    print(message.sticker.file_id)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Русский язык
    if message.text == '🇷🇺 Русский':
        print('Посетил бот - ' + message.chat.username)
        logging.info('Start bot - ' + message.chat.username)
        print(message.chat.username)
        print('_____________________')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn2 = types.KeyboardButton('📢 Вакансии')
        btn5 = types.KeyboardButton('📝 Оставить заявку')
        btn1 = types.KeyboardButton("🌐 Сайт")
        btn3 = types.KeyboardButton('📁 Проекты')
        btn4 = types.KeyboardButton('📚 Блог')
        btn7 = types.KeyboardButton('👥 Мы в ВК')
        btn8 = types.KeyboardButton('🔥 Мы на Хабр')
        btn9 = types.KeyboardButton('🅱️ Мы на Behance')
        btn12 = types.KeyboardButton('📸 Мы в Instagram')
        btn10 = types.KeyboardButton('✍️️ Мы на LinkedIn')
        btn11 = types.KeyboardButton('🔙 Вернуться к выбору языка')
        markup.add(btn2, btn5, btn1, btn3, btn4, btn7, btn8, btn9, btn10, btn12)
        bot.send_message(message.from_user.id, "👋 Вас приветствует бот компании Fusion Tech", reply_markup=markup)
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')

    if message.text == 'русский':
        print('Посетил бот')
        print(message.chat.username)
        print('_____________________')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn2 = types.KeyboardButton('📢 Вакансии')
        btn5 = types.KeyboardButton('📝 Оставить заявку')
        btn1 = types.KeyboardButton("🌐 Сайт")
        btn3 = types.KeyboardButton('📁 Проекты')
        btn4 = types.KeyboardButton('📚 Блог')
        btn7 = types.KeyboardButton('👥 Мы в ВК')
        btn8 = types.KeyboardButton('🔥 Мы на Хабр')
        btn9 = types.KeyboardButton('🅱️ Мы на Behance')
        btn12 = types.KeyboardButton('📸 Мы в Instagram')
        btn10 = types.KeyboardButton('✍️️ Мы на LinkedIn')
        btn11 = types.KeyboardButton('🔙 Вернуться к выбору языка')
        markup.add(btn2, btn5, btn1, btn3, btn4, btn7, btn8, btn9, btn10, btn12)
        bot.send_message(message.from_user.id, "👋 Вас приветствует бот компании Fusion Tech", reply_markup=markup)
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')

    if message.text == 'Русский':
        print('Посетил бот')
        print(message.chat.username)
        print('_____________________')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn2 = types.KeyboardButton('📢 Вакансии')
        btn5 = types.KeyboardButton('📝 Оставить заявку')
        btn1 = types.KeyboardButton("🌐 Сайт")
        btn3 = types.KeyboardButton('📁 Проекты')
        btn4 = types.KeyboardButton('📚 Блог')
        btn7 = types.KeyboardButton('👥 Мы в ВК')
        btn8 = types.KeyboardButton('🔥 Мы на Хабр')
        btn9 = types.KeyboardButton('🅱️ Мы на Behance')
        btn12 = types.KeyboardButton('📸 Мы в Instagram')
        btn10 = types.KeyboardButton('✍️️ Мы на LinkedIn')
        btn11 = types.KeyboardButton('🔙 Вернуться к выбору языка')
        markup.add(btn2, btn5, btn1, btn3, btn4, btn7, btn8, btn9, btn10, btn12)
        bot.send_message(message.from_user.id, "👋 Вас приветствует бот компании Fusion Tech", reply_markup=markup)
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел')
    elif message.text == '🔙 Вернуться к выбору языка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🇷🇺 Русский")
        btn2 = types.KeyboardButton('🇬🇧 English')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)

    elif message.text == '🌐 Сайт':
        logging.info('Открыт раздел сайт, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Посетить веб-сайт", setting.website))
        bot.send_message(message.from_user.id,
                         'Наша гордость - наша история.👍 Перейти к сайту можно по ссылке ' + setting.website,
                         reply_markup=markup2, parse_mode='HTML')
    elif message.text == '📢 Вакансии':
        logging.info('Открыт раздел Вакансии, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Менеджер по продажам (Sales Manager)')
        btn2 = types.KeyboardButton('UI/UX дизайнер')
        btn3 = types.KeyboardButton('Разработчик Fullstack')
        btn4 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id,
                         'Раздел: 📢 Вакансии\n \n👍🏻 Хочешь создавать лучшее?\n Тогда нам по пути! \n📲 Перейти к разделу можно по ссылке ' + setting.vacansies,
                         reply_markup=markup, parse_mode='HTML')
        bot.send_message(message.from_user.id, '⬇ Открытые вакансии', reply_markup=markup)

    elif message.text == 'Менеджер по продажам (Sales Manager)':
        logging.info('Открыт раздел Менеджер по продажам, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Открыть вакансию", setting.SALES_MANAGER))
        bot.send_message(message.from_user.id,
                         'Менеджер по продажам (Sales Manager) -->>> Перейти к вакансии можно по ссылке ' + setting.SALES_MANAGER,
                         reply_markup=markup2, parse_mode='HTML')

    elif message.text == 'UI/UX дизайнер':
        logging.info('Открыт раздел дизайнер, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Открыть вакансию", setting.DESIGN))
        bot.send_message(message.from_user.id,
                         'UI/UX дизайнер -->>> Перейти к разделу можно по ссылке ' + setting.DESIGN,
                         reply_markup=markup2, parse_mode='HTML')

    elif message.text == 'Разработчик Fullstack':
        logging.info('Открыт раздел Разработчик, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Открыть вакансию", setting.DEV_FULL))
        bot.send_message(message.from_user.id,
                         'Разработчик Fullstack -->>> Перейти к разделу можно по ссылке ' + setting.DEV_FULL,
                         reply_markup=markup2, parse_mode='HTML')

    elif message.text == '📁 Проекты':
        logging.info('Открыт раздел Проекты, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Посмотреть наши проекты", setting.projects))
        bot.send_message(message.from_user.id,
                         'Раздел: 🚀 Проекты\n \n👍🏻📲 Перейти к разделу можно по ссылке ' + setting.projects,
                         reply_markup=markup2, parse_mode='HTML')

    elif message.text == '📚 Блог':
        logging.info('Открыт раздел Блог, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Почитать наш блог", setting.blog))
        bot.send_message(message.from_user.id,
                         'Раздел: 📚 Блог\n \n👍🏻 Свежие новости студии, работа и идеи\n \n📲 Перейти к разделу можно по ссылке ' + setting.blog,
                         reply_markup=markup2, parse_mode='HTML')

    elif message.text == '🔙 Главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn2 = types.KeyboardButton('📢 Вакансии')
        btn5 = types.KeyboardButton('📝 Оставить заявку')
        btn1 = types.KeyboardButton("🌐 Сайт")
        btn3 = types.KeyboardButton('📁 Проекты')
        btn4 = types.KeyboardButton('📚 Блог')
        btn7 = types.KeyboardButton('👥 Мы в ВК')
        btn8 = types.KeyboardButton('🔥 Мы на Хабр')
        btn9 = types.KeyboardButton('🅱️ Мы на Behance')
        btn12 = types.KeyboardButton('📸 Мы в Instagram')
        btn10 = types.KeyboardButton('✍️️ Мы на LinkedIn')
        btn11 = types.KeyboardButton('🔙 Вернуться к выбору языка')
        markup.add(btn2, btn5, btn1, btn3, btn4, btn7, btn8, btn9, btn10, btn12)
        bot.send_message(message.from_user.id, "👀 Выбери интересующий раздел", reply_markup=markup)

    elif message.text == '👥 Мы в ВК':
        logging.info('Открыт раздел ВК, юзер -' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('🕵🏼 Написать Даше (HR компании)')
        btn2 = types.KeyboardButton('✏️ Написать нам')
        btn3 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '⬇ Выбери то, что тебе интересно', reply_markup=markup)
        bot.send_message(message.from_user.id,
                         'Перейти к группе ВК можно по ссылке ' + setting.VK,
                         reply_markup=markup, parse_mode='HTML')
    # Small talk

    elif message.text == 'Привет!':
        bot.send_message(message.from_user.id, 'Привет!')

    elif message.text == 'привет!':
        bot.send_message(message.from_user.id, 'Привет!')

    elif message.text == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')

    elif message.text == 'как дела?':
        bot.send_message(message.from_user.id, 'Хорошо!')

    elif message.text == 'Как дела?':
        bot.send_message(message.from_user.id, 'Хорошо!')

    elif message.text == 'как дела':
        bot.send_message(message.from_user.id, 'Хорошо!')

    elif message.text == 'отмена':
        bot.send_message(message.from_user.id, 'Отменено пользователем!')
        start()

    elif message.text == 'Отмена':
        bot.send_message(message.from_user.id, 'Отменено пользователем!')
        start()

    elif message.text == '/stop':
        bot.send_message(message.from_user.id, 'Отменено пользователем!')
        start()

    elif message.text == 'Заявка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn2 = types.KeyboardButton('📢 Вакансии')
        btn5 = types.KeyboardButton('📝 Оставить заявку')
        bot.send_message(message.from_user.id, 'Оставьте заявку для дальнейшего собеседования', reply_markup=markup)
        markup.add(btn2, btn5)

    elif message.text == 'заявка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn2 = types.KeyboardButton('📢 Вакансии')
        btn5 = types.KeyboardButton('📝 Оставить заявку')
        bot.send_message(message.from_user.id, 'Оставьте заявку для дальнейшего собеседования', reply_markup=markup)
        markup.add(btn2, btn5)

    elif message.text == 'собеседование':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn2 = types.KeyboardButton('📢 Вакансии')
        btn5 = types.KeyboardButton('📝 Оставить заявку')
        bot.send_message(message.from_user.id, 'Оставьте заявку для дальнейшего собеседования', reply_markup=markup)
        markup.add(btn2, btn5)

    elif message.text == 'работа':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn2 = types.KeyboardButton('📢 Вакансии')
        btn5 = types.KeyboardButton('📝 Оставить заявку')
        bot.send_message(message.from_user.id, 'Оставьте заявку для дальнейшего собеседования', reply_markup=markup)
        markup.add(btn2, btn5)

    elif message.text == 'вакансии':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn2 = types.KeyboardButton('📢 Вакансии')
        btn5 = types.KeyboardButton('📝 Оставить заявку')
        bot.send_message(message.from_user.id, 'Оставьте заявку для дальнейшего собеседования', reply_markup=markup)
        markup.add(btn2, btn5)

    elif message.text == 'хочу на собеседование':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn2 = types.KeyboardButton('📢 Вакансии')
        btn5 = types.KeyboardButton('📝 Оставить заявку')
        bot.send_message(message.from_user.id, 'Оставьте заявку для дальнейшего собеседования', reply_markup=markup)
        markup.add(btn2, btn5)

    elif message.text == 'пока':
        bot.send_message(message.from_user.id, 'Всего доброго, заходите еще')

    elif message.text == 'Пока':
        bot.send_message(message.from_user.id, 'Всего доброго, заходите еще')

    elif message.text == 'Новости':
        bot.send_message(message.from_user.id,
                         'Раздел: 📚 Блог\n \n👍🏻 Свежие новости студии, работа и идеи\n \n📲 Перейти к разделу можно по ссылке ' + setting.blog,
                         parse_mode='HTML')

    elif message.text == 'новости':
        bot.send_message(message.from_user.id,
                         'Раздел: 📚 Блог\n \n👍🏻 Свежие новости студии, работа и идеи\n \n📲 Перейти к разделу можно по ссылке ' + setting.blog,
                         parse_mode='HTML')

    elif message.text == '🕵🏼 Написать Даше (HR компании)':
        logging.info('Открыт раздел Написать Даше, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'По вопросу трудоустройства и стажировок пиши в сообщество, нашему HR Дарье по ссылке ' + setting.VK_HR,
                         reply_markup=markup, parse_mode='HTML')

    elif message.text == '✏️ Написать нам':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         'По общим вопросам пиши нам в сообщество, по ссылке ' + setting.VK_GROUP_CHAT,
                         reply_markup=markup, parse_mode='HTML')

    elif message.text == '✍️️ Мы на LinkedIn':
        logging.info('Открыт раздел LinkedIn, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Перейти к нам на страницу", setting.LINKEDIN))
        bot.send_message(message.from_user.id, '\n Перейти к разделу можно по ссылке ' + setting.LINKEDIN,
                         reply_markup=markup2, parse_mode='HTML')

    elif message.text == '🅱️ Мы на Behance':
        logging.info('Открыт раздел Behance, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Перейти к нам на страницу", setting.BEHANCE))
        bot.send_message(message.from_user.id,
                         'With our expertise,we can suggest the best solutions for your project to make it as good as possible.'
                         '\n Перейти к разделу можно по ссылке ' + setting.BEHANCE,
                         reply_markup=markup2, parse_mode='HTML')

    elif message.text == '📸 Мы в Instagram':
        logging.info('Открыт раздел Instagram, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        markup2 = types.InlineKeyboardMarkup()
        markup2.add(types.InlineKeyboardButton("Перейти к нам на страницу", setting.INSTAGRAM))
        bot.send_message(message.from_user.id,
                         '🏆ТОП-100 работодателей России // Хабр Карьера'
                         '\n📍Taganrog // Yerevan // Claymont'
                         '\n Перейти к разделу можно по ссылке ' + setting.INSTAGRAM,
                         reply_markup=markup2, parse_mode='HTML')

    elif message.text == '🔥 Мы на Хабр':
        logging.info('Открыт раздел Хабр, юзер - ' + message.chat.username)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        btn2 = types.KeyboardButton('Страница компании')
        btn3 = types.KeyboardButton('📰 Вакансии')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id,
                         'Найди работу по душе 🎉 \n В базе Хабр Карьеры всегда актуальные вакансии компании'
                         '\n Перейти к разделу можно по ссылке ' + setting.HABR,
                         reply_markup=markup, parse_mode='HTML')

    elif message.text == 'Страница компании':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id,
                         "Мы Fusion Tech - компания, уже более 5-ти лет предоставляющая качественные веб и мобильные продукты, клиентский сервис, а также пропуск в мир IT через бесплатную стажировку в компании под наставничеством опытных кураторов.")
        bot.send_message(message.from_user.id,
                         'Почитать более подробно, а также подписаться на нашу компанию можно по ссылке ' + setting.HABR,
                         reply_markup=markup, parse_mode='HTML')

    elif message.text == '📝 Оставить заявку':
        logging.info('Старт заявки' + message.chat.username)
        chat_id = message.chat.id
        msg = bot.send_message(chat_id, "Добрый день, представьтесь пожалуйста.")
        bot.register_next_step_handler(msg, name_step)


def name_step(message, user=None):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        msg = bot.send_message(chat_id, "Укажите ваш возраст")
        bot.register_next_step_handler(msg, process_age_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_age_step(message):
    try:
        chat_id = message.chat.id
        age = message.text
        if not age.isdigit():
            msg = bot.send_message(chat_id, 'Возраст должен быть числом, введи его повторно: ')
            bot.register_next_step_handler(msg, process_age_step)
            return
        user = user_dict[chat_id]
        user.age = age
        msg = bot.send_message(chat_id, 'К какой специализации вы относитесь?', )

        bot.register_next_step_handler(msg, process_spec_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_spec_step(message):
    try:
        chat_id = message.chat.id
        language = message.text
        user = user_dict[chat_id]
        user.languages = language
        msg = bot.send_message(chat_id, 'Локация')
        bot.register_next_step_handler(msg, process_location_step)
    except Exception as e:
        bot.reply_to(message, 'Непредвиденная ошибка')


def process_location_step(message):
    try:
        chat_id = message.chat.id
        location = message.text
        user = user_dict[chat_id]
        user.location = location
        msg = bot.send_message(chat_id, 'Формат работы (удаленно/офис)')
        bot.register_next_step_handler(msg, process_format_work_step)
    except Exception as e:
        bot.reply_to(message, 'Непредвиденная ошибка')


def process_format_work_step(message):
    try:
        chat_id = message.chat.id
        format_work = message.text
        user = user_dict[chat_id]
        user.format_work = format_work
        msg = bot.send_message(chat_id, 'Опыт работы?')
        bot.register_next_step_handler(msg, process_experience_step)
    except Exception as e:
        bot.reply_to(message, 'Непредвиденная ошибка')


def process_experience_step(message):
    try:
        chat_id = message.chat.id
        experience = message.text
        user = user_dict[chat_id]
        user.experience = experience
        msg = bot.send_message(chat_id,
                               'Вставьте ссылку на ваш профиль(GitHub,Behance,Dribbble,Figma,VK) если нет - напишите нет: ')
        bot.register_next_step_handler(msg, process_git_acc_step)
    except Exception as e:
        bot.reply_to(message, 'Непредвиденная ошибка')


def process_git_acc_step(message):
    try:
        chat_id = message.chat.id
        git_acc1 = message.text
        user = user_dict[chat_id]
        user.git_acc = git_acc1
        msg = bot.send_message(chat_id, "Контактные данные")
        bot.register_next_step_handler(msg, contnums)

    except Exception as e:
        bot.reply_to(message, 'Непредвиденная ошибка')


def contnums(message):
    try:
        chat_id = message.chat.id
        nums = message.text
        user = user_dict[chat_id]
        user.nums = nums
        chat_id = message.chat.id
        msg = bot.send_message(chat_id, "Основные навыки")
        bot.register_next_step_handler(msg, send_z)
    except Exception as e:
        bot.reply_to(message, 'Непредвиденная ошибка')


def send_z(message):
    chat_id = message.chat.id
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    user_name = message.chat.username
    z = message.text  # text user
    app_text = []
    app_name_first = []
    app_name_last = []
    app_username = []
    app_name_first.append(first_name)
    app_name_last.append(last_name)
    app_username.append(user_name)
    app_text.append(z)
    user = user_dict[chat_id]
    user_chats = message.from_user.id
    bot.send_message(setting.admin_id_ugraswim, f'Поступил новый отклик от {app_name_first[0]} {app_name_last[0]} !\n'
                     + f'username в тг = @{app_username[0]} \n'
                     + f'Возраст  -  {user.age} \n'
                     + f'Локация  -  {user.location} \n'
                     + f'Опыт работы  -  {user.experience} \n'
                     + f'Специализация: {user.languages} \n'
                     + f'Основные навыки: - {app_text[0]} \n'
                     + f'Профиль github/социальная сеть  -  {user.git_acc} \n'
                     + f'Формат работы  -  {user.format_work} \n'
                     + f'Контактные данные: {user.nums} \n'

                     + f'ID юзера: {user_chats}')
    # bot.send_message(setting.admin_hr_id, f'Поступил новый отклик от {app_name_first[0]} {app_name_last[0]} !\n'
    #                  + f'username в тг = @{app_username[0]} \n'
    #                  + f'Возраст  -  {user.age} \n'
    #                  + f'Локация  -  {user.location} \n'
    #                  + f'Опыт работы  -  {user.experience} \n'
    #                  + f'Специализация: {user.languages} \n'
    #                  + f'Основные навыки: - {app_text[0]} \n'
    #                  + f'Профиль github/социальная сеть  -  {user.git_acc} \n'
    #                  + f'Формат работы  -  {user.format_work} \n'
    #                  + f'Контактные данные: {user.nums} \n'
    #
    #                  + f'ID юзера: {user_chats}')
    conn = psycopg2.connect(dbname='db/fusion_bot', user='Fusion', password='root', host='localhost')
    cursor = conn.cursor()
    user = user_dict[chat_id]
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders(
            id INTEGER,
            user_first_name TEXT,
            user_last_name TEXT,
            username TEXT
            location TEXT
            special TEXT
            nums TEXT
            );''')
    conn.commit()
    id_people = message.from_user.id
    cursor.execute(f"SELECT id FROM orders WHERE id = {id_people}")
    data = cursor.fetchone()
    if data is None:
        order = [message.from_user.id,
                 message.from_user.first_name,
                 message.from_user.last_name,
                 message.from_user.username,
                 user.location,
                 user.languages,
                 user.nums]
        cursor.execute("INSERT INTO orders VALUES(?,?,?,?,?,?,?);", order)
        conn.commit()
    else:
        print("Такой ID пользователя уже есть в базе данных")
        logging.warning('Хотел оставить заявку, но уже оставлял - ' + message.chat.username)
    app_name_first.clear()
    app_name_last.clear()
    app_username.clear()
    app_text.clear()
    logging.info('Заявка успешно отправлена от - ' + message.chat.username)
    bot.send_message(chat_id, "Заявка отправлена, мы свяжемся с Вами в ближайшее время")


try:
    bot.infinity_polling(timeout=90, long_polling_timeout=5)
except (ConnectionError, ReadTimeout) as e:
    sys.stdout.flush()
    os.execv(sys.argv[0], sys.argv)
else:
    bot.infinity_polling(timeout=90, long_polling_timeout=5)
