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
    # print(repr(title))
    price = product.find('span', {'class':'product__price'}).text.strip() #split('\n')[0]
    # print(price)
    images = product.find('a', {'class':"product__image-wrapper"}).find_all('img')
    # image_1 = [i.get('srcset') for i in 
    for i in images:
        print(i.get('srcset'))
    # dict_data = {'title': title, 'price': price, 'image_1' : url + image, 'image_2' : ''}
    # print(image_1)
    # return {
    # 'title': title, 
    # 'price': price, 
    # 'image_1' : url + image, 
    # 'image_2' : ''}

def write_to_json(data:dict):
    with open('zhora.json', 'w', encoding='utf-8') as file:
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
    # dict_data = {'title': title, 'price': price, 'image_1' : url + image, 'image_2' : ''}
    # write_to_json(res)
    return res
print(get_all_products_from_page('https://ugmonk.com/collections/clothing'))



# def write_to


# def get_last_page(url : str) -> int:
#     soup = get_soup(url)
#     last = soup.find('li', {'class' : 'last'})
#     return int(last.text)


# def main():
#     # category = '/commercialsearch/all/?type=6'
#     data = {}
#     # last_page = get_last_page(BASE_URL + category)
#     # for page in range(1,last_page + 1):
#     #     url = BASE_URL + category + '?page=' + str(page)
#     #     print(url)
#     #     one_page_data = get_all_products_from_page(url)
#     #     data[page] = one_page_data
#     write_to_json(data)
# main()

with open('articles.json', 'w') as f:
    # for post in all_posts:
    #     date = post.h2.text
    #     title = post.h3.text
    #     body = post.find('div', 'post-body entry-content').text
    f.writelines([])




