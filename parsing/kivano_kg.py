from bs4 import BeautifulSoup as bs 
import requests 
import json


telephones_name = []
telephones_price = []
telephones_price_res = []
telephones_result = []

count = 0
page = 1

while True:
    URL = 'https://www.kivano.kg/mobilnye-telefony?page='

    html = requests.get(URL + str(page)).text
    soup = bs(html, 'lxml')

    telephones = soup.find_all('div', class_ = 'item product_listbox oh')
    
    for telephon in telephones:
        telephones_name.append(telephon.find('img').get('alt'))
        telephones_price.append(telephon.find('div', class_="listbox_price text-center").text)
        telephones_price_res.append(telephones_price[count].strip().replace('\n', ''))
        print(len(telephones_name))
        count += 1

    if page == 19:
        break

    page += 1
    

total = 1
with open('telephones_price.json', 'a') as file:
    for t, p in zip(telephones_name, telephones_price_res):
        telephones_result.append({'Номер': total, 'Название': t, 'Цена': p})
        total += 1

        
    json.dump(telephones_result, file, ensure_ascii=False, indent=2)
