import requests
from bs4 import BeautifulSoup as BS

source = requests.get('https://tvoe.ru/catalog/jenshchinam/dlinsovaya-odezhda/').text
soup = BS(source, 'lxml')

def get_product() -> dict:
    title = soup.find('div', class_="product__title-block").text
    price = 
print(get_product())