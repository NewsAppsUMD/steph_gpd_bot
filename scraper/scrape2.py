from bs4 import BeautifulSoup
import csv
import tabula
import sqlite_utils
import datasette_codespaces

url = 'https://www.greenbeltmd.gov/i-want-to/view/weekly-crime-report/-folder-1474'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

soup = BeautifulSoup(html, features="html.parser")
ul = soup.find_all('ul')[-1]

#set up a container for all my records
list_of_rows = []
#start my loop
for li in ul.find_all('li'):
    #find the a tags, which is where the info is
    for a in li.find_all('a'):
        #set up a container for the date and url that will go in each row
        each_row = []
        if li.find('a'):
            #in cases where there is an a tag in the list item, put together a url for the href inside the a tag and also print out the text in that a tag (which is the date)
            #print("https://www.greenbeltmd.gov" + li.find('a')['href'], li.text)
            #appending the elements described in above note to each_row
            each_row.append("https://www.greenbeltmd.gov" + li.find('a')['href'])
            each_row.append(li.text)

writer.writerow(["url", "date"])
writer.writerows(list_of_rows)

data=[]
for row in list_of_rows:
    df = tabula.read_pdf(list_of_rows, pages="all")
    data.append(df)
print(data)