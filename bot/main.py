import telebot
from bs4 import BeautifulSoup as bs
import requests

bot = telebot.TeleBot('7491704349:AAH_vDZzsGHCvZukczODY5ik4Ut2vlaR_1k')
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn1 = telebot.types.KeyboardButton('1', )
btn2 = telebot.types.KeyboardButton('1', )
btn1 = telebot.types.KeyboardButton('1', )
btn1 = telebot.types.KeyboardButton('1', )
btn1 = telebot.types.KeyboardButton('1', )
btn1 = telebot.types.KeyboardButton('1', )
btn1 = telebot.types.KeyboardButton('1', )
btn1 = telebot.types.KeyboardButton('1', )
btn1 = telebot.types.KeyboardButton('1', )
btn1 = telebot.types.KeyboardButton('1', )
btn1 = telebot.types.KeyboardButton('1', )
btn1 = telebot.types.KeyboardButton('1', )
btn1 = telebot.types.KeyboardButton('1', )
btn1 = telebot.types.KeyboardButton('1', )
btn1 = telebot.types.KeyboardButton('1', )
btn1 = telebot.types.KeyboardButton('1', )
btn1 = telebot.types.KeyboardButton('1', )
btn1 = telebot.types.KeyboardButton('1', )
btn1 = telebot.types.KeyboardButton('1', )
btn1 = telebot.types.KeyboardButton('1', )

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Вот первые 20 новостей')
    news(message)

def news(message):
    URL = 'https://kaktus.media/?lable=8&date=2025-03-19&order=time'
    html = requests.get(URL).text
    soup = bs(html, 'lxml')

    vse_news = soup.find_all('div', class_="Tag--article")[:20]
    links = []

    count = 1
    for i in vse_news:
        news_name = i.find('a', class_="ArticleItem--name").text.strip()
        photo = 'https://kaktus.media' + i.find('img').get('src')
        links.append(i.find('a').get('href'))
        bot.send_message(message.chat.id, f'№ {count}\nновость - {news_name}\n Ссылка на фото  {photo}')
        count += 1
    msg = bot.send_message(message.chat.id, 'Выберите какую новость хотите почитать (выберите от 1 до 20)')
    bot.register_next_step_handler(msg, nomer_news)

def nomer_news():
    ...



bot.polling(non_stop=True)

    

