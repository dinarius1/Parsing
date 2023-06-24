#Task 1

#неправильный вариант
# import requests
# source = requests.get('https://stackoverflow.com/questions')
# print(source.status_code)

# правильный вариант:
import requests 
source = requests.get('https://stackoverflow.com/questions').status_code 
print(source)

#Task 2
import requests
from bs4 import BeautifulSoup
sourse = requests.get('http://www.example.com/').text
soup = BeautifulSoup(sourse, 'lxml')
print(f"h1: {soup.h1.text}")
print(f"p: {soup.p.text}")
print(f"a: {soup.a.get('href')}")

#Task 3

import requests
from bs4 import BeautifulSoup
source = requests.get('https://www.wikipedia.org/').text
soup = BeautifulSoup(source, 'lxml')
language = soup.find('div', class_ = 'central-featured-lang lang4').find('a').find('strong').text
number = soup.find('div', class_ = 'central-featured-lang lang4').find('a').find('small').find('bdi').text
artical = soup.find('div', class_ = 'central-featured-lang lang4').find('a').find('small').find('span').text
# soup.find('div',{'class_' : 'central-featured-lang lang4'}.find('lang4') - почему, когда так пишешь выходит ошибка,

print(f'{language} \n{number} {artical}')

#Task 4
import requests
from bs4 import BeautifulSoup
def getTitle(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml').find('h1')
    if soup == None:
        return 'Title could not be found'
    return soup

# print(getTitle('https://www.w3resource.com/'))
print(getTitle('http://www.example.com/'))


# Задание 5

import requests
from bs4 import BeautifulSoup
import csv



source = requests.get('https://enter.kg/').text
soup = BeautifulSoup(source, 'lxml')


res = soup.find('div', class_="moduletable").find_all('li', class_="VmClose")

category_list = [el.find('a').text for el in res if el.find('a') != None]

def find_category(categories, keyword):
    all_category = [el.text.strip() for el in res if el.find('a') != None]
    dict_ = dict(zip(category_list,all_category))
    for k,v in dict_.items():
        if keyword.lower() in k.lower():
            return v


with open('enterkg.csv', 'a') as csv_file:
    res3 = find_category(category_list, "Процессоры")
    writer = csv.writer(csv_file)
    writer.writerow(list(res3))

print(find_category(category_list, 'Процессоры'))

# print(category_list)
# def find_category(categories, keyword):
#     all_list1 = 1

#     res2 = []
#     for el in categories:
#         if el.lower().startswith(keyword.lower()):
#             res2.append(el)
#     return res2

# print(find_category(category_list, 'Ноутбуки'))

# Задание 6
    
import requests
from bs4 import BeautifulSoup

source = requests.get('https://www.imdb.com/chart/top').text
soup = BeautifulSoup(source, 'lxml')

titles = soup.find('div', class_="lister").find('table').find_all('td', class_="titleColumn")

title_list = [el.find('a').text for el in titles]
print(title_list)

def get_link(title_list, name : str):
    main_url = 'https://www.imdb.com'
    film_links = [main_url + el.find('a').get('href') for el in titles]
    dict_ = dict(zip(title_list, film_links))

    for n, link in dict_.items():
        if name.lower() in n.lower():
            return link

print(get_link(title_list, 'shawshank'))


# films = {'The Shawshank Redemption': 'https://www.imdb.com/title/tt0111161/', 'The Godfather': 'https://www.imdb.com/title/tt0068646/'}


# # name = 'shawshank'

# # for n, link in films.items():
# #     if name.lower() in n.lower():
# #         print(link)



