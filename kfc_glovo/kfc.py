import json
import requests
from bs4 import BeautifulSoup as BS


BASE_URL = 'https://glovoapp.com/kg/ru/bishkek/kfc-bsk-kg/?content=sousy-dopolnitelnye-produkty-c.602138715'

def get_soup(url:str) -> BS:
    response = requests.get(url)
    soup = BS(response.text, 'lxml')
    return soup

def get_product_info(product: BS) -> dict:
    # url = 'https:'
    title = product.find('span').text.strip()
    # print(title)
    price = product.find('span', {'class':'product-price__effective'}).text.strip().split("\xa0")[0]
    print(price)
    # description = product.find('span', class_="product-row__info__description").text.strip()
    # print(description)
    image = product.find('div', {'class':"product-row__content"}).find('img').get('srcset').split()[0]
    # print(image)
    return {
    'title': title, 
    'price': price + ' KGS', 
    'image' : image}

'''
Создаем функцию, которая позволяла бы записывать данные в формате json
data - это параметр, который мы должны передать при вызове этой функции
'''
def write_to_json(data:dict):
    with open('glovo.json', 'a+', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii= False)


def get_all_products_from_page(url:str) -> list:
    res = []
    soup = get_soup(url)
    box = soup.find('div', {'class' : "store__body__dynamic-content"})
    # print(box)
    products = box.find_all('div', {'type':"PRODUCT_ROW"})
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
print(get_all_products_from_page('https://glovoapp.com/kg/ru/bishkek/kfc-bsk-kg/?content=sousy-dopolnitelnye-produkty-c.602138715'))

