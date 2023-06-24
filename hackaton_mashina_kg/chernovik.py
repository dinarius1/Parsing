import requests
from bs4 import BeautifulSoup as BS

# BASE_URL = 'https://www.mashina.kg'

response = requests.get('https://www.mashina.kg/commercialsearch/all/?type=6').text
soup = BS(response, 'lxml')


def get_last_page(url : str) -> int:
    pages = soup.find_all('li', {'class' : "page-item"})[-1].find('a').get('data-page')

    # l = pages[-3].text.strip('\n').strip().split()
    # last_page = l[0]
    # return int(last_page)
    return int(pages)
print(get_last_page('https://www.mashina.kg/commercialsearch/all/?type=6'))

# title = soup.find('div', class_="search-results-table").
# title = soup.find_all('h2')
# t = [el.text.strip() for el in title]
# print(t)

# box_price = soup.find_all('div',class_='list-item')
# price = [el[0] +'\n'+el[-1].lstrip() for el in p]
# p = soup.find('div',class_='list-item').find('p').text.strip().split('\n')
# price = p[0] +'\n'+p[-1].lstrip()
# print(repr(price))

# один элемент - p = soup.find('div',class_='list-item').find('p').text.strip().split('\n')
# price = p[0] +'\n'+p[-1].lstrip()
# image = soup.find('div', class_="list-item list-label new-line").find('img').get('data-src')
# image_el = [el for el in image]

# discription_1 = soup.find('p', class_="year-miles").text.strip('\n').strip()
# # discription_2 = soup.find('i', class_="color-icon")
# discription_2 = soup.find('p', class_="body-type").text.strip('\n').strip()
# discription_3 = soup.find('p', class_="volume").text.strip('\n').strip()
# all_discription = discription_1 + ' ' + discription_2 + ' ' + discription_3
# # d1 = [el.text.strip('\n').strip() for el in discription]
# print(p)

# pages = soup.find_all('li', {'class' : "page-item"})
# l = pages[-3].text.strip('\n').strip().split()
# last_page = l[0]
# print(last)