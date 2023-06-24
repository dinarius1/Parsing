import requests
from bs4 import BeautifulSoup as BS
from datetime import date
import csv

BASE_URL = 'https://kaktus.media'

today = str(date.today())
# today = '2023-06-24'
# print(today)

#Создаем динамичную ссылку
category = '/?lable=8&date='+ today + '&order=time'
all_link = BASE_URL + category

#Получаем весь код со страницы
def get_soup(url:str) -> BS:
    response = requests.get(url)
    soup = BS(response.text, 'lxml')
    return soup

#Получаем информацию в текстовом виде
def get_news_info(el: BS) -> dict:
    title = el.find('a', {'class' : 'ArticleItem--name'}).text.strip()
    return title

#Записываем результат в csv файл   
def write_csv(data):
    with open('kaktus.csv', 'a', newline= '', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter='.')
        for page_num, article_title in data.items():
            writer.writerow([page_num, article_title])

#Вытащим заголовки первых 20 статьей и их номера 
def all_news() -> list:
    soup = get_soup('https://kaktus.media/?lable=8&date=' + today + '&order=time')
    box = soup.find('div', {"class": "Tag--articles"})
    news = box.find_all('div', {'class':"ArticleItem--data"})
    all_titles_news = []
    for el in news:
        news_info = get_news_info(el)
        all_titles_news.append(news_info)
    numbers = [i for i in range(1,21)]
    dict_ = dict(zip(numbers,all_titles_news))
    write_csv(dict_)
    return dict_

all_news()