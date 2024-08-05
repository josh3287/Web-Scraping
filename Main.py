import requests
from bs4 import BeautifulSoup


url = 'https://www.astrofreightdispatch.com/'
r = requests.get(url)
r