import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.greenbeltmd.gov/i-want-to/view/weekly-crime-report/-folder-1474'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content


soup = BeautifulSoup(html, features="html.parser")
ul = soup.find_all('ul')[-1]

list_of_rows = []
for row in ul.find_all('li'):
    list_of_cells = []
    for cell in row.find_all('a'):
        if cell.find('a'):
            list_of_cells.append(cell.text)
            list_of_cells.append("https://www.greenbeltmd.gov" + cell.find('a')['href'])
    text = cell.text.strip()
    list_of_cells.append(text)
list_of_rows.append(list_of_cells)
print(list_of_rows)






       



    
    
        
    
    






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