from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
 
url = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBoun' \
      'ds%22%3A%7B%22west%22%3A-122.67559818816567%2C%22east%22%3A-121.80928490949059%2C%22south%22%3A37.22014619' \
      '453056%2C%22north%22%3A37.839879124127194%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price' \
      '%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C' \
      '%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7' \
      'D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Af' \
      'alse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value' \
      '%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'
 
headers = { 
            'Accept-Language' : "en-US,en;q=0.5",
            'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0"
        }
 
class DataEntry:
    def __init__(self):
        # self.driver = webdriver.Chrome(executable_path=path)
        self.header = headers
 
    def get_houses(self):
        # requests
        response = requests.get(url=url, headers=self.header)
        content = response.text
 
        # scraping
        soup = BeautifulSoup(content, 'html.parser')
        houses_card = soup.find_all(class_='list-card-info', name='div')
 
        data = [{
            'price': house.findChild('div', class_='list-card-price').text[:6],
            'url': house.findChild('a').get('href') if house.findChild('a').get('href').startswith('h') else f"https://www.zillow.com/{house.findChild('a').get('href')}",
            'address':  house.findChild('a').text
        } for house in houses_card]
 
        return data

a = DataEntry()
print(a.get_houses())

