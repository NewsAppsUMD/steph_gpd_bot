import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.greenbeltmd.gov/i-want-to/view/weekly-crime-report/-folder-1474'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content


soup = BeautifulSoup(html, features="html.parser")
ul = soup.find_all('ul')[-1]

list_of_rows = []
for li in ul.find_all('li'):
    for a in li.find_all('a'):
        if li.find('a'):
            list_of_rows.append(li.text)
            list_of_rows.append("https://www.greenbeltmd.gov" + li.find('a')['href'])
print(list_of_rows)

#list_of_rows = []
#for row in ul.find_all('li'):
    #list_of_cells = []
    #for cell in row.find_all('a'):
        #if cell.find('a'):
            #list_of_cells.append("https://www.greenbeltmd.gov" + cell.find('a')['href'])
    #print(list_of_cells)
        #if cell.find(text)
            #list_of_cells.append(cell.text)
    #text = cell.text.strip()
    #list_of_cells.append(text)
#list_of_rows.append(list_of_cells)
#print(list_of_rows)






       



    
    
        
    
    






