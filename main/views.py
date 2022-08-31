# coding: utf-8
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import telebot
from bot.bot import bot, InlineKeyboard
from bot.models import *
from settings import development


@csrf_exempt
def get_message(request):
    if request.method == 'POST':
        json_string = request.body.decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        print(request, 'GET_MESSAGE')
        return HttpResponse('!', 200)
    return HttpResponse('Method Not Allowed', 405)


bot.set_webhook(url=f'92.255.76.200/{development.BOT_TEST_TOKEN}')
