import json
import requests
from bs4 import BeautifulSoup as BS

BASE_URL = 'https://www.kivano.kg'

def get_soup(url:str) -> BS:
    response = requests.get(url)
    soup = BS(response.text, 'lxml')
    return soup

def get_product_info(product: BS) -> dict:
    title = product.find('div', {'class' : 'listbox_title'}).text.strip()
    print(title)
    # print(repr(title))
    price = product.find('div', {'class':'listbox_price'}).text.strip().split('\n')[0]
    # print(price)
    image = product.find('div', class_="list-item list-label new-line").find('img').get('data-src')
    # print(image)
    return {'title': title, 'price': price, 'image' : BASE_URL + image}




def get_all_products_from_page(url:str) -> list:
    res = []
    soup = get_soup(url)
    box = soup.find('div', {'class': 'list-view'})
    print(box)
    products = box.find_all('div', {'class': 'product_listbox'})
    # print(len(products))
    for product in products:
        product_info = get_product_info(product)
        res.append(product_info)
    return res
print(get_all_products_from_page('https://www.kivano.kg'))

# def write_to_json(data:dict):
#     with open('db.json', 'w', encoding='utf-8') as file:
#         json.dump(data, file, ensure_ascii= False)

def get_last_page(url : str) -> int:
    soup = get_soup(url)
    last = soup.find('li', {'class' : 'last'})
    return int(last.text)


def main():
    category = '/commercialsearch/all/?type=6'
    data = {}
    last_page = get_last_page(BASE_URL + category)
    for page in range(1,last_page + 1):
        url = BASE_URL + category + '?page=' + str(page)
        print(url)
        one_page_data = get_all_products_from_page(url)
        data[page] = one_page_data
    write_to_json(data)
main()




