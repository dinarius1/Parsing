import requests
from bs4 import BeautifulSoup as BS
import csv

BASE_URL = 'https://www.mashina.kg'

#Получаем весь код со страницы
def get_soup(url:str) -> BS:
    response = requests.get(url)
    soup = BS(response.text, 'lxml')
    return soup

#Записываем данные в csv файл   
def write_csv(data):
    with open('db.csv', 'a', newline= '', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

#Получаем полную информацию о продукте
def get_product_info(product) -> dict:
    # product = get_soup('https://www.mashina.kg/commercialsearch/all/?type=6&page=1')
    title = product.find('h2').text.strip()
    p = product.find('p').text.strip().split('\n')
    price = p[0] +'\n'+p[-1].lstrip()
    image = product.find('img').get('data-src') 
    discription_1 = product.find('p', class_="year-miles").text.strip('\n').strip()
    discription_2 = product.find('p', class_="body-type").text.strip('\n').strip()
    discription_3 = product.find('p', class_="volume").text.strip('\n').strip()
    all_discription = discription_1 + ' ' + discription_2 + ' ' + discription_3
    data = [title, price, image, all_discription]
    write_csv(data)
    return data
# print(get_product_info())

#Получаем все товары со страницы
def get_all_products_from_page(url:str) -> list:
    res = []
    soup = get_soup(url)
    box = soup.find('div', class_="table-view-list")
    products = box.find_all('div', class_="list-item")
    for product in products:
        product_info = get_product_info(product)
        res.append(product_info)
    return res

#Создаем динамичный код по поиску последней страницы на сайте продукта
def get_last_page(url : str) -> int:
    soup = get_soup(url)
    last_page = soup.find_all('li', {'class' : "page-item"})[-1].find('a').get('data-page')
    return int(last_page)

#Главная функция
def main():
    category = '/commercialsearch/all/?type=6'
    last_page = get_last_page(BASE_URL + category)
    data = []
    for page in range(1,last_page + 1):
        url = BASE_URL + category + '&page=' + str(page)
        one_page_data = get_all_products_from_page(url)
        data.append(one_page_data)

print(main())

