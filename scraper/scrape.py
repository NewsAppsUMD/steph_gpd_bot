import requests
from bs4 import BeautifulSoup

url = 'https://www.greenbeltmd.gov/i-want-to/view/weekly-crime-report/-folder-1474'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content
print(html)

soup = BeautifulSoup(html, features="html.parser")
table = soup.find('ul')
print(table.prettify())
# to run python scraper/scrape.py