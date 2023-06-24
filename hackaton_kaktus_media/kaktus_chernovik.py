import requests
from bs4 import BeautifulSoup as BS
import datetime
#начала делать хакатон в 14.47

BASE_URL = 'https://kaktus.media'

now = datetime.datetime.now()
now2 = str(now).split()
date_now = now2[0]

category = '/?lable=8&date='+ date_now + '&order=time'
all_link = BASE_URL + category

def get_soup(url:str) -> BS:
    response = requests.get(url)
    soup = BS(response.text, 'lxml')
    return soup

def get_news_info(el: BS) -> dict:
    title = el.find('a', {'class' : 'ArticleItem--name'}).text.strip()
    discription = el.find('a', {'class' : 'ArticleItem--name'}).get('href')
    image = el.find('img', {'class' : 'ArticleItem--image-img ls-is-cached lazyloaded'}).get('data-src')
    # return [title,[discription, image]]
    return image
print(get_news_info)

# def details_news():
    

#вытащим заголовки всех статей и номера всех статьей
def all_news() -> list:
    soup = get_soup('https://kaktus.media/?lable=8&date=2023-03-11&order=time')
    box = soup.find('div', {"class": "Tag--articles"})
    news = box.find_all('div', {'class':"ArticleItem--data"})
    # titles_news = [el.find('a', {'class' : 'ArticleItem--name'}).text.strip() for el in news] 
    all_titles_news = []
    for el in news:
        news_info = get_news_info(el)
        all_titles_news.append(news_info)
    numbers = [i for i in range(1,21)]
    dict_ = dict(zip(numbers,all_titles_news))
    return dict_
# print(all_news())


