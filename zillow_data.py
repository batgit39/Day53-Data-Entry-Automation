import re
from bs4 import BeautifulSoup
import requests

URL = ("https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D")

class Zillow():

    def __init__(self) -> None:

        header = { 
                    'Accept-Language' : "en-GB,en-US;q=0.9,en;q=0.8",
                    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
                }
        response = requests.get(url= URL, headers=header)
        response.raise_for_status()
        website_data = response.text

        self.soup = BeautifulSoup(website_data, 'html.parser')

    def get_prices(self):
        prices = self.soup.find_all(attrs={"data-test": "property-card-price"})
        return [element.getText() for element in prices]

    def get_address(self):
        addresses = self.soup.find_all(attrs={"data-test": "property-card-addr"})
        final_addresses = []
        for address in addresses:
            stripped_address = address.getText()
            if "|" in stripped_address:
                stripped_address = stripped_address.split("|")[1].strip()
            final_addresses.append(stripped_address)
            
        return final_addresses

    def get_links(self):
        links = self.soup.select(selector=".property-card-data a")
        final_links = []
        for link in links:
            stripped_link = str(link)
            stripped_link = stripped_link.split('"')[5]
            https_search = re.search("^https.", stripped_link)
            if https_search:
                pass
            else:
                stripped_link = "https://www.zillow.com" + stripped_link
            final_links.append(stripped_link)
         
        return final_links

