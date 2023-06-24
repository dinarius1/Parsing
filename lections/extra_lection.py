import requests
from bs4 import BeautifulSoup as BS

"============================Пагинация в mashina.kg============================"
# "Пагинация" - от слова страинцы, нахождение послежней страницы
BASE_URL = "https://www.mashina.kg/search/all/"

html = requests.get(BASE_URL).text
soup = BS(html, 'lxml')
pagination = soup.find('ul', {'class' : 'pagination'})
last_li = pagination.find_all('li')[-1]
last_page = last_li.find('a').get('data-page')  #get - позволяет вытащить любое занчения атрибута
print(last_page) 

"======================================CSV======================================"
import csv
data = [
    {'title':"hello", "price":342},
    {'title':"test", "price":7643},
    {'title':"aaa", "price":324},
    {'title':"bbb", "price":453},
]

with open('test.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter= ',')    
    #дастаем метод writer таким образом   
    # #delimiter - разделитель
    writer.writerow(data[0].keys) #это заголовки для столбиков
    #выводиv только ключи 1 элемента в списке data -> title, price
    for product in data:
        writer.writerow(product.values()) #вызываем у writer метод writerow, который позволяет записывать данные в виде
