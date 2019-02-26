﻿import json
import requests
from Menu import MenuPlan

TELE_TOKEN = 'PLACE-YOUR-TOKEN-HERE'
URL = "https://api.telegram.org/bot{}/".format(TELE_TOKEN)

# Define some cool emojis that can be used in the return strings
PIZZA = u'\U0001F355'
BURGER = u'\U0001F354'
PASTA = u'\U0001F35D'
CHICKEN = u'\U0001F357'


# Define the funciton that shall be executed on Start command /start, which is automatically send when starting the bot
def start():
    # Sending some welcome messages and instructions about the bot usage
    return PIZZA + BURGER + '_Wellkomme bem Foodbot vo de UZH!_' + CHICKEN + PASTA + '\n\nSchriib mer eifach de Name vo de Mensa ond de Wochetag, ond ech scheck der de aktuelli Menüplan zrogg!\n\nVerfüegbar send: *Zentrum | Irchel | Binz | Rämi | Platte* \nBiispel: Irchel Ziistig, Binz, Zentrum morn'


# Function that is being executed when /help is requested by the user
def help():
    # send back  help instructions
    return 'Schriib de Name vo de Mensa, vo wellere du s Menü wetsch gseh: *Zentrum | Irchel | Binz | Rämi | Platte*, ond en Ziitponkt wie: *hött | öbermorn | friitig*, etc.'


# Function reads the users messages and returns the requested menu plan
def mensa(msg):
    try:
        response = MenuPlan(msg).get()
    except Exception as e:
        response = "Upps, do esch leider en Fehler passiert.. " + u'\U0001F623' + '\n' + str(e)
    return response


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode=markdown".format(text, chat_id)
    print(url)
    requests.get(url)

def lambda_handler(event, context):
    message = json.loads(event['body'])
    chat_id = message['message']['chat']['id']
    msg = message['message']['text']

    if msg == "/start":
        send_message(start(), chat_id)
    elif msg == "/help":
        send_message(help(), chat_id)
    else:
        send_message(mensa(msg), chat_id)
    return {
        'statusCode': 200
    }

if __name__ == "__main__":
    msg = "binz"
    chat_id = -1

    if msg == "/start":
        send_message(start(), chat_id)
    elif msg == "/help":
        send_message(help(), chat_id)
    else:
        send_message(mensa(msg), chat_id)