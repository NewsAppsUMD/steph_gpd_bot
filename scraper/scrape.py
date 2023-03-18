import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.greenbeltmd.gov/i-want-to/view/weekly-crime-report/-folder-1474'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content


soup = BeautifulSoup(html, features="html.parser")
ul = soup.find_all('ul')[-1]
list_of_links = []
for li in ul.find_all('li'):
    if li.find('a'):
        list_of_links.append("https://www.greenbeltmd.gov" + li.find('a')['href'])
        list_of_dates = []
        list_of_dates.append(li.text)
        #print(list_of_dates)
        #print(list_of_links)
        table = zip(list_of_dates, list_of_links)
        outfile = open('./reports.csv', 'w')
        writer = csv.writer(outfile)
        writer.writerows(table)



    
    
        
    
    






#print(list_of_links)

        
        
        #if a.find_all('href'):
            #print(href)
        
        #print(a)



#if li.find('a'):
        #list_of_li.append("https://www.greenbeltmd.gov" + li.find('a')['href'])



    #list_of_cells = []
    #for a in li.find_all('a'):
        #print('a')


# to run python scraper/scrape.py