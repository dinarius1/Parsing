import requests
from bs4 import BeautifulSoup  #BeautifulSoup - это новый класс, новый тип данных

main_url = 'https://www.kivano.kg/'

response = requests.get(main_url)  #отправляем запрос 
# print(dir(response))
# print(response.text) #html - str

soup = BeautifulSoup(response.text, 'lxml')
# print(dir(soup))

phones_span = soup.find('span', {'id': 'phones'})
# print(phones_span)

raw_phones = phones_span.text
phones_list = []

for ph in raw_phones.split('\n'):
    clear_phone = ph.replace('\r', '').strip()
    if clear_phone:
        phones_list.append(clear_phone)

# print(phones_list)

"========================Детализация продукта========================"
product_url = "product/view/sotovyy-telefon-apple-iphone-14-pro-256gb-fioletovyy"

response = requests.get(main_url + product_url)
# print(response)
soup = BeautifulSoup(response.text, 'lxml')

product_card = soup.find('div', {'class' : 'product-view'})
# print(product_card)

title = product_card.find('h1').text   #text - это перменная, которая позволяет вывести весь текст между тегами
# print(title)

# print(product_card.find_all('img'))  #find_all - метод, который выводит все теги с этим словом

image_box = product_card.find('div', {'class' : 'img_full'})
image = image_box.find('img').get('src')
# print(image)

price = product_card.find('span', {'itemprop' : 'price'}).text
print(price)

data = {'title' : title, 'image' :  image, 'price' : price}
print(data)