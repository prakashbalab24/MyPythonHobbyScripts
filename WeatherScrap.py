import os
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

baseUrl = 'https://weather.com/en-IN/weather/today/l/INXX0012:1:IN'
req = Request(baseUrl, headers={'User-Agent': 'Mozilla/5.0'})

page = urlopen(req)

soup = BeautifulSoup(page, 'html.parser')
city_temp = soup.find('div',attrs={'class':'today_nowcard-temp'})
city_name = soup.find('h1',attrs={'class':'today_nowcard-location'})
city_cmd = soup.find('div',attrs={'class':'today_nowcard-phrase'})

print(city_name.text)
print (city_temp.text)
print(city_cmd.text)

notify(city_name.text,city_temp.text +" "+city_cmd.text)
