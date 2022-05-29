# -*- coding: utf-8 -*-
# Подключаем модуль случайных чисел 
import random
# Подключаем модуль для Телеграма
import telebot
# Указываем токен
bot = telebot.TeleBot('5075120530:AAHRMuVcFHazuKTzSYZq6wZ-f2bPINHN-Eo')
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
# Заготовки для трёх предложений
first = ["Сегодня — идеальный день для новых начинаний."]
second = ["Человек - это то, о чем он думает в течение дня"]
second_add = ["Все будет хорошо, если к этому стремиться"]
third = ["Каждый день нужно делать шаги к успешному будщему"]
# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text == "Здравствуйте":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "Здравствуйте, сейчас я расскажу вам, чем могу помочь.")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого ответа
        key_1 = types.InlineKeyboardButton(text='Подача документов', callback_data='school')
        # И добавляем кнопку на экран
        keyboard.add(key_1)
        key_2 = types.InlineKeyboardButton(text='Программа обучения', callback_data='school')
        keyboard.add(key_2)
        key_3 = types.InlineKeyboardButton(text='Дополнительные кружки', callback_data='school')
        keyboard.add(key_3)
        key_4 = types.InlineKeyboardButton(text='Состав учителей', callback_data='school')
        keyboard.add(key_4)
        key_5 = types.InlineKeyboardButton(text='Администрация', callback_data='school')
        keyboard.add(key_5)
        key_6 = types.InlineKeyboardButton(text='Спортивные достижения', callback_data='school')
        keyboard.add(key_6)
        key_7 = types.InlineKeyboardButton(text='Как связаться с директором', callback_data='school')
        keyboard.add(key_7)
        key_s8 = types.InlineKeyboardButton(text='Часы работы', callback_data='school')
        keyboard.add(key_8)
        key_9 = types.InlineKeyboardButton(text='Адрес школы', callback_data='school')
        keyboard.add(key_9)
        key_10 = types.InlineKeyboardButton(text='Отзывы выпускников и родителей', callback_data='school')
        keyboard.add(key_10)
        key_11 = types.InlineKeyboardButton(text='Медалисты', callback_data='school')
        keyboard.add(key_11)
        key_12 = types.InlineKeyboardButton(text='Рейтинг среди других школ города Волжск', callback_data='school')
        keyboard.add(key_12)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выберите интересующий вас вопрос', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Здравствуйте")
    else:
        bot.send_message(message.from_user.id, "Я вас не понимаю. Напишите /help.")
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == "school": 
        # Формируем гороскоп
        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)
