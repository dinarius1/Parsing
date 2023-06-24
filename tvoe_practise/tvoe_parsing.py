import requests
from bs4 import BeautifulSoup as BS

source = requests.get('https://tvoe.ru/').text
soup = BS(source, 'lxml')

title_list = soup.find('div', class_="menu__dropdown").find_all('a', class_="submenu__item-link text-h6")

# 1. Название катологов
all_title = [el.text.strip() for el in title_list]

# 2. Название подкаталогов
inner_titles = soup.find('ul', class_="submenu submenu--sublevel").find_all('div', class_="submenu__item-caption")

all_inners = [el.text.strip() for el in inner_titles]

