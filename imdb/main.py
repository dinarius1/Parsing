import requests
from bs4 import BeautifulSoup

source = requests.get('https://www.imdb.com/chart/top').text
soup = BeautifulSoup(source, 'lxml')

titles = soup.find('div', class_="lister").find('table').find_all('td', class_="titleColumn")

title_list = [el.find('a').text for el in titles]
# print(title_list)

def get_link(title_list, name : str):
    main_url = 'https://www.imdb.com'
    film_links = [main_url + el.find('a').get('href') for el in titles]
    dict_ = dict(zip(title_list, film_links))

    for n, link in dict_.items():
        if name.lower() in n.lower():
            return link

print(get_link(title_list, 'shawshank'))
