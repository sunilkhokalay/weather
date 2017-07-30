from urllib import request
from bs4 import BeautifulSoup

class Weather(object):
    BASE_URL = "https://weather.com/en-IN/weather/today/l/"

    def __init__(self,city='bengaluru'):
        self.city = city
        self.bengaluru = "INXX0012:1:IN"
        self.url = Weather.BASE_URL+self.bengaluru

    def getTemp(self):
        handle = request.urlopen(self.url)
        soup = BeautifulSoup(handle,"html.parser")
        current_temp = soup.findAll("span", {"class": "deg-feels"})[0]
        return int((current_temp.text)[:-1])



