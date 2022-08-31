# -*- coding: utf-8 -*-
import telebot
from telebot import types
import csv

token_bot = '5715779093:AAFOW_jCCja7xLx51qMPvnvqkJkq2JrrLB0'
bot = telebot.TeleBot(token_bot)

flag_buyed = 0
id_user = ''
username = ''
fullname = ''

'''base_data_of_user = []
with open('data/base_data_of_user.csv', 'r', encoding='utf8') as fr:
    cread = csv.reader(fr, delimiter=';')

    for i in cread:
        base_data_of_user.append(i)


list_expect = []
with open('data/list_expect.csv', 'r', encoding='utf8') as fr:
    cread = csv.reader(fr, delimiter=';')

    for i in cread:
        list_expect.append(i)


def upd():

    with open('data/base_data_of_user.csv', 'w', encoding='utf8') as fw:
        fwr = csv.writer(fw, delimiter=';', lineterminator="\r")

        fwr.writerow(['id', 'username', 'fullname', 'private_pass', 'day_lost'])
        for el in base_data_of_user[1:]:
            fwr.writerow(el)


def upd_expect():

    with open('data/list_expect.csv', 'w', encoding='utf8') as fw:
        fwr = csv.writer(fw, delimiter=';', lineterminator="\r")

        fwr.writerow(['id', 'username', 'expect'])
        for el in list_expect[1:]:
            fwr.writerow(el)


@bot.message_handler(commands=['start'])
def start_bot(message):
    global base_data_of_user
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton('Тарифы')
    btn2 = types.KeyboardButton('Private status')
    btn3 = types.KeyboardButton('Menu')

    markup.add(btn1, btn2, btn3)

    get_full_data_of_user(message)

    flag = 0
    for el in base_data_of_user[1:]:
        if id_user == int(el[0]):
            flag = 1
            break

    if flag == 0:
        base_data_of_user.append(
            [id_user, username, '', 0, '']
        )
        upd()

    bot.send_message(message.from_user.id, ''.join(open('data/start_message', 'r').readlines()), reply_markup=markup)
    bot.send_message(message.from_user.id, 'Чтобы оплатить тариф напиши название тарифа\n'
                                           'FOREVER')
    bot.send_message(message.from_user.id, 'Ознакомиться с тарифами можно ниже\n' +
                                            ''.join(open('data/tarif', 'r').readlines()))


def tariph(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn4 = types.KeyboardButton('Forever')
    btn5 = types.KeyboardButton('Я оплатил')
    btn6 = types.KeyboardButton('Menu')

    markup.add(btn4, btn5, btn6)

    bot.send_message(message.from_user.id, 'Ознакомиться с тарифом можно ниже\n' +
                                           ''.join(open('data/tarif', 'r').readlines()), reply_markup=markup)


@bot.message_handler(commands=['forever'])
def buy_private_forever(message):
    global flag_buyed

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn4 = types.KeyboardButton('Forever')
    btn5 = types.KeyboardButton('Я оплатил')
    btn6 = types.KeyboardButton('Menu')

    markup.add(btn4, btn5, btn6)

    flag_buyed = 1
    get_full_data_of_user(message)

    text = 'Тариф: FOREVER\n' \
           'Стоимость: 249р\n' \
           f'Ваш id: {id_user}\n' \
           'Срок: Навсегда\n\n' \
           'Вы получите доступ в канал - Hot клубничка приват 18+\n\n' \
           'Тут ты найдешь много интересного и горячего контента: \n' \
           '     -Tenderbite, -Karna.val, -W.bery, -di.tsm, -HannahOwo, -Aweshc,\n' \
           '     -LexusLife, -Sharishanya, -Marianna_moss и много другого)\n\n' \
           'Контент собираем с известных источников таких, как:\n' \
           'Fansly, Onlyfans, и покупаем приватки,\n\n' \
           'Оплата на Qiwi счёт: +7-913-480-90-14\n' \
           f'В комментарии под заказом ОБЯЗАТЕЛЬНО ПРОПИСАТЬ ваш id - ({id_user})\n' \
           f'ИНАЧЕ ОПЛАТА НЕ ПРОЙДЕТ\n\n' \
           '!!ПОСЛЕ ОПЛАТЫ НАПИШИТЕ (Я ОПЛАТИЛ) В ЧАТ!!\n\n' \
           'Если доступ не откроется через 15 минут\n' \
           'напишите - @m0nke3'
    bot.send_message(message.from_user.id, text, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.text == 'Private dostup' or message.text == '/private' or 'Private status' == message.text:
        check_private(message)
    if message.text.upper() == 'FOREVER':
        buy_private_forever(message)
    if message.text.lower() == 'я оплатил':
        expect(message)
    if message.text == 'Тарифы':
        tariph(message)
    if message.text.lower() == 'menu':
        start_bot(message)


def expect(msg):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Тарифы')
    btn2 = types.KeyboardButton('Private status')
    btn3 = types.KeyboardButton('Menu')

    markup.add(btn1, btn2, btn3)

    get_full_data_of_user(msg)
    if flag_buyed:
        bot.send_message(msg.from_user.id, 'Через 15 минут нажмите на команду /private или Private status\n'
                                           'для проверки изменения вашего статуса\n'
                                           'там же найдете ссылку на канал', reply_markup=markup)

        list_expect.append(
            [id_user, username, msg.text]
        )
        upd_expect()
    else:
        bot.send_message(msg.from_user.id, 'Сначало выберите тариф!', reply_markup=markup)


def get_full_data_of_user(message):
    global id_user, username, fullname

    id_user = message.from_user.id
    username = message.from_user.username


@bot.message_handler(commands=['private'])
def check_private(message):
    global base_data_of_user

    get_full_data_of_user(message)

    name = username
    if name is None:
        name = 'Друг'

    text = f'Привет {name}\n\n' \
           f'к сожалению ты еще не приобрел доступ в приват('

    for el in base_data_of_user[1:]:
        id_, usname, fllname, private, day_lost = el
        if int(id_) == int(id_user):
            if private == '1':
                text = f'Привет {name}!\n' \
                       f'Твоя подписка активна!\n\n' \
                       f'Ссылка на канал: https://t.me/+Z04WmPiZiBUwNzgy'

    bot.send_message(message.from_user.id, text)'''


@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)
