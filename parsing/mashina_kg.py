from bs4 import BeautifulSoup as bs
import requests 
import json 

URL = 'https://m.mashina.kg/'

html = requests.get(URL).text
soup = bs(html, 'lxml')

# Легковые авто
cars = soup.find('div', class_="category-block cars").find_all('div', class_="category-block-content-item")
leg_cars_name = []
leg_cars_price = []
leg_name_price = []
leg_img = []
for car in cars:
    leg_cars_name.append(car.find('div', class_="main-title").text.strip())
    leg_cars_price.append(car.find('span', class_ = 'currency-1').text.strip())
    leg_img.append(car.find('img').get('src'))

count = 1
for c, p, i in zip(leg_cars_name, leg_cars_price,leg_img):
    leg_name_price.append({'№': count,'Название': c, 'Цена': p, 'Ссылка на фото': i})
    count += 1


# Коммерческие авто 
commer_avto = soup.find('div', class_ = 'category-block commercial').find_all('div', class_="category-block-content-item")
commer_cars_name = []
commer_cars_price = []
commer_name_price = []
commer_img = []

for car in commer_avto:
    commer_cars_name.append(car.find('div', class_="main-title").text.strip().replace('\n                                                                    ', ' - '))
    commer_cars_price.append(car.find('span', class_="currency-1").text.strip())
    commer_img.append(car.find('img').get('src'))
count1 = 1
for n, p, i in zip(commer_cars_name, commer_cars_price, commer_img):
    commer_name_price.append({'№': count1,'Название': n, 'Цена': p, 'Ссылка на фото': i})
    count1 += 1

# # Спецтехника 
spex_cars = soup.find('div', class_="category-block spec").find_all('div', class_="category-block-content-item")
spex_name = []
spex_price = []
spex_name_price = []
spex_img = []

for car in spex_cars:
    spex_name.append(car.find('div', class_="main-title").text.strip().replace('\n                                                                    ', ' - '))
    spex_price.append(car.find('span', class_="currency-1").text.strip())
    spex_img.append(car.find('img').get('src'))
count2 = 1
for n, p, i in zip(spex_name, spex_price, spex_img):
    spex_name_price.append({'№': count2,'Название': n, 'Цена': p, 'Ссылка на фото': i})  
    count2 += 1

# Запчасти
spare_parts = soup.find('div', class_="category-block parts").find_all('div', class_="category-block-content-item")
spare_name = []
spare_price = []
spare_name_price = []
spare_img = []

for car in spare_parts:
    spare_name.append(car.find('div', class_="main-title").text.strip())
    spare_img.append(car.find('img').get('src'))
    try:
        spare_price.append(car.find('span', class_="currency-1").text.strip())
    except:
        spare_price.append('Договорная')

count3 = 1
for n, p, i in zip(spare_name, spare_price, spare_img):
    spare_name_price.append({'№': count3,'Название': n, 'Цена': p, 'Ссылка на фото': i})
    count3 += 1


# Услуги
uslugi = soup.find('div', class_="category-block service").find_all('div', class_="category-block-content-item")
uslugi_name = []
uslugi_price = []
uslugi_name_price = []
uslugi_img = []
for car in uslugi:
    uslugi_name.append(car.find('div', class_="main-title").text.strip())
    uslugi_img.append(car.find('img').get('src'))
    try:
        uslugi_price.append(car.find('span', class_="currency-1").text.strip())
    except:
        uslugi_price.append('Договорная')

count4 = 1
for n, p, i in zip(uslugi_name, uslugi_price, uslugi_img):
    uslugi_name_price.append({'№': count4,'Название': n, 'Цена': p, 'Ссылка на фото': i})
    count4 += 1

# Мото 
moto = soup.find('div', class_="category-block moto").find_all('div', class_="category-block-content-item")
moto_name = []
moto_price = []
moto_name_price = []
moto_img = []

for car in moto:
    moto_name.append(car.find('div', class_="main-title").text.strip().replace('\n                                                                    ', ' - '))
    moto_img.append(car.find('img').get('src'))
    try:
        moto_price.append(car.find('span', class_="currency-1").text.strip())
    except:
        moto_price.append('Договорная')

count5 = 1
for n, p, i in zip(moto_name, moto_price, moto_img):
    moto_name_price.append({'№': count5,'Название': n, 'Цена': p, 'Ссылка на фото': i})
    count5 += 1

# Куплю
buy = soup.find('div', class_="category-block buy").find_all('div', class_="category-block-content-item")
buy_name = []
buy_price = []
buy_name_price = []
buy_img = []

for car in buy:
    buy_name.append(car.find('div', class_="main-title").text.strip().replace('\n                                                                    ', ' - '))
    buy_img.append(car.find('img').get('src'))
    try:
        buy_price.append(car.find('span', class_="currency-1").text.strip())
    except:
        buy_price.append('Договорная')

count6 = 1
for n, p, i in zip(buy_name, buy_price, buy_img):
    buy_name_price.append({'№': count6,'Название': n, 'Цена': p, 'Ссылка на фото': i})
    count6 += 1

# Результат 
cars_result  = []

cars_result.append({'Легковые авто': leg_name_price})
cars_result.append({'Коммерческие авто':commer_name_price})
cars_result.append({'Спецтехники': spex_name_price})
cars_result.append({'Запчасти': spare_name_price})
cars_result.append({'Услуги': uslugi_name_price})
cars_result.append({'Мото': moto_name_price})
cars_result.append({'Куплю': buy_name_price})


# Добавление в JSON
with open('mashina_kg.json', 'a') as file:
    json.dump(cars_result, file, ensure_ascii=False, indent= 2)


