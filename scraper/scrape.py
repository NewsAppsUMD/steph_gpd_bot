import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.greenbeltmd.gov/i-want-to/view/weekly-crime-report/-folder-1474'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content


soup = BeautifulSoup(html, features="html.parser")
ul = soup.find_all('ul')[-1]

#set up a container for all my records
list_of_rows = []
#start my loop
for li in ul.find_all('li'):
    for a in li.find_all('a'):
        each_row = []
        if li.find('a'):
            print(li.text, "https://www.greenbeltmd.gov" + li.find('a')['href'])
    list_of_rows.append(each_row)
    print(list_of_rows)
            


        
            
#outfile = open('./reports.csv', 'w')
#writer = csv.writer(outfile)
#writer.writerows(list_of_rows)

