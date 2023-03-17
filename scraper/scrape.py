import requests
from bs4 import BeautifulSoup

url = 'https://www.greenbeltmd.gov/i-want-to/view/weekly-crime-report/-folder-1474'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content


soup = BeautifulSoup(html, features="html.parser")
ul = soup.find_all('ul')[-1]
for li in ul.find_all('li'):
    for a in li.find_all('a'):
        list_of_links = []
        for link in a.find('href'):
            list_of_links.append("https://www.greenbeltmd.gov" + link.find('href'))
print(list_of_links)

        
        
        #if a.find_all('href'):
            #print(href)
        
        #print(a)



#if li.find('a'):
        #list_of_li.append("https://www.greenbeltmd.gov" + li.find('a')['href'])



    #list_of_cells = []
    #for a in li.find_all('a'):
        #print('a')


# to run python scraper/scrape.py