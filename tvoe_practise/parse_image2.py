import requests

image_url = 'https://tvoe.ru/img/c4t6ec/product/626/834/36/4620123670797.jpg'

image = requests.get(image_url)
with open('tvoe.jpg', 'wb') as file:
    file.write(image.content)