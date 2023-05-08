from zillow_data import Zillow
from google_form import Google_forms

zillow = Zillow()
prices = zillow.get_prices()
links = zillow.get_links()
address = zillow.get_address()

forms = Google_forms()
forms.send_data(prices, address, links)
