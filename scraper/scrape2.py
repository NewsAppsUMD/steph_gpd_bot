from bs4 import BeautifulSoup
import csv
import tabula
import sqlite_utils
import datasette_codespaces
import requests

url = 'https://www.greenbeltmd.gov/i-want-to/view/weekly-crime-report/-folder-1474'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

soup = BeautifulSoup(html, features="html.parser")
ul = soup.find_all('ul')[-1]

#inside the loop, create an empty dictionary: dict = {} and populate it with each url and date. Then append dict to your urls_with_dates

#set up a container for all my records
urls_with_dates = []
#start my loop
for li in ul.find_all('li'):
    #find the a tags, which is where the info is
    for a in li.find_all('a'):
        #set up a container for my dictionaries, which will include the dates and urls to put in my urls_and_dates container
        dict={}
        if li.find('a'):
            dict['url'] = "https://www.greenbeltmd.gov" + li.find('a')['href']
            dict['date'] = a.get_text()
        #print(dict)
    urls_with_dates.append(dict)
#print(urls_with_dates)

for each in urls_with_dates:
    df = tabula.read_pdf(each['url'], pages="all")
    tabula.convert_into(each['url'], "output.csv", pages="all")
    #print(df)
