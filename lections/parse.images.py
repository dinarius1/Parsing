import requests, json

image_url = 'https://s9.travelask.ru/uploads/post/000/005/619/main_image/full-3ac4aa56dc92d34df054283e565b28a0.jpg'

response = requests.get(image_url)

with open('test.jpg', 'wb') as file:
    file.write(response.content)