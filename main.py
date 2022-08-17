import requests
import random
import telebot
from bs4 import BeautifulSoup as b
from config import SECRET_TOKEN

URL = 'http://www.anekdot.ru/last/good/'
API_KEY = 'SECRET_TOKEN'
def parser(url):
    r = requests.get(URL)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('div', class_='text')
    return [c.text for c in anekdots]

list_of_anekdo = parser(URL)
random.shuffle(list_of_anekdo)

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['start'])
def start(message):
    mess  = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name} Введи цифру: </b>'
    bot.send_message(message.chat.id, mess , parse_mode='html')

@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_of_anekdo[0])
        del list_of_anekdo[0]
    else:
         bot.send_message(message.chat.id, "Введите любую цифру:")


bot.polling(none_stop=True)