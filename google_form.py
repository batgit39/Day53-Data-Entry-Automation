from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

form_link = ""
# make a google form and add your link

class Google_forms():

    def __init__(self): 
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options = self.options, service= Service('/home/mitresh/Development-Selenium/chromedriver'))
        # add your chromedriver link
        # driver.maximize_window()

    def send_data(self, prices, address, links):
        self.prices = prices
        self.address = address
        self.links = links
        for i in range(len(self.prices)):
            self.driver.get(form_link)
            time.sleep(3)
            address_field = self.driver.find_element(by="xpath", value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
            address_field.send_keys(self.address[i])
            # time.sleep(2)
            price_field = self.driver.find_element(by="xpath", value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
            price_field.send_keys(self.prices[i])
            # time.sleep(2)
            link_field = self.driver.find_element(by="xpath", value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
            link_field.send_keys(self.links[i])
            # time.sleep(2)
            submit_button = self.driver.find_element(by="xpath", value="//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div")
            submit_button.click()
            time.sleep(3)

        self.driver.quit()
