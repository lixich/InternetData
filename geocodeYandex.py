#https://tech.yandex.ru/maps/geocoder/
import requests
url = 'https://geocode-maps.yandex.ru/1.x/'
r = requests.get(url, params = {'geocode': 'Пермь, Техническая, 22', 'format':'json'})
print(r.json())
print(r.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'])
