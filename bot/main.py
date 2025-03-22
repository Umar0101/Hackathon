import telebot
from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime

bot = telebot.TeleBot('7491704349:AAH_vDZzsGHCvZukczODY5ik4Ut2vlaR_1k')

keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn1 = telebot.types.KeyboardButton('Закрыть')
keyboard.add(btn1)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Вот последние 20 новостей')
    news(message)

def news(message):
    time = datetime.now().strftime('%Y-%m-%d')
    try:
        URL = f'https://kaktus.media/?lable=8&date={time}&order=time'
        html = requests.get(URL).text
        soup = bs(html, 'lxml')

        vse_news = soup.find_all('div', class_="Tag--article")[:20]
        links = []
        photo_list = []
        twelwe_news = []
        count = 1
        for i in vse_news:
            news_name = i.find('a', class_="ArticleItem--name").text.strip()
            photo = i.find('img').get('src')
            time = i.find('div', class_="ArticleItem--time").text.strip()
            photo_list.append(photo)
            links.append(i.find('a').get('href'))
            twelwe_news.append(f'№ {count} \nВремя - {time} \n{news_name} \n{photo}')
            count += 1
        for news in twelwe_news:
            bot.send_message(message.chat.id, news)
            
        msg = bot.send_message(message.chat.id, 'Выберите какую новость, хотите почитать (выберите от 1 до 20)')
        bot.register_next_step_handler(msg, nomer_news, links, twelwe_news, photo_list)
    except:
        bot.send_message(message.chat.id, 'Не удалось получить информацию. Пожалуйста, попробуйте позже.')

def nomer_news(message, links, twelwe_news, photo_list):

    try:
        user_num = int(message.text)
        if user_num < 1 or user_num > 20:
            msg1 = bot.send_message(message.chat.id, 'Вы ввели несуществующий номер. Попробуйте снова ввести число от 1 до 20.')
            bot.register_next_step_handler(msg1, nomer_news, links, twelwe_news, photo_list)   
        elif user_num >= 1 and user_num <= 20:
            index = user_num - 1
            html = requests.get(links[index]).text
            soup = bs(html, 'lxml')
            description = soup.find('div', class_="BbCode").find('p').text.strip()
            bot.send_message(message.chat.id, f'{twelwe_news[index]}\n<b>Краткое описание</b>: {description}', parse_mode='html')
            photo = photo_list[index]
            bot.send_photo(message.chat.id, photo)
            msg = bot.send_message(message.chat.id, 'Если хотите завершить, нажмите кнопку "Закрыть" \nЕсли хотите почитать другую новость, выберите (от 1 до 20)', reply_markup=keyboard)
            bot.register_next_step_handler(msg, nomer_news, links, twelwe_news, photo_list)
    except:
        if message.text.lower() == 'закрыть':
            bot.send_message(message.chat.id, 'До свидания! Для запуска бота отправьте команду /start.', reply_markup=telebot.types.ReplyKeyboardRemove())
        
    
bot.polling(non_stop=True)

    

