import requests

city = 'Lagos'
url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=7f29e00623a297702809f6d7138d3d85'



r = requests.get(url.format(city)).json()
print(r)

new = r['main']['temp']

print(new)
