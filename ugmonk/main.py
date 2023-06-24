import json
import requests
from bs4 import BeautifulSoup as BS


BASE_URL = 'https://ugmonk.com/collections/clothing'

def get_soup(url:str) -> BS:
    response = requests.get(url)
    soup = BS(response.text, 'lxml')
    return soup

def get_product_info(product: BS) -> dict:
    url = 'https:'
    title = product.find('h2', class_= "product__title").text.strip()
    # print(title)
    price = product.find('span', {'class':'product__price'}).text.strip()
    image_1 = product.find('a', {'class':"product__image-wrapper"}).find('img').get('srcset')
    return {
    'title': title, 
    'price': price, 
    'image_1' : url + image_1, 
    'image_2' : ''}

'''
Создаем функцию, которая позволяла бы записывать данные в формате json
data - это параметр, который мы должны передать при вызове этой функции
'''
def write_to_json(data:dict):
    with open('ugmonk.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii= False)


def get_all_products_from_page(url:str) -> list:
    res = []
    soup = get_soup(url)
    box = soup.find('div', {'class' : "row row--gutters products"})
    # print(box)
    products = box.find_all('div', {'class':"product__content"})
    # print(products)
    for product in products:
        product_info = get_product_info(product)
        res.append(product_info)
    '''
    Мы тут вызываем функцию  write_to_json, которую мы создали до этого
    Внутри этой функции мы указываем, что нужно переопределить в формат json. В нашем случае это res - словарь с продуктами которую мы получили из функции 
    '''
    get_product_info(product)
    write_to_json(res)
    return res
print(get_all_products_from_page('https://ugmonk.com/collections/clothing'))







