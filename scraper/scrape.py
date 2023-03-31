import requests
from bs4 import BeautifulSoup
import csv
import tabula
import pandas as pd

url = 'https://www.greenbeltmd.gov/i-want-to/view/weekly-crime-report/-folder-1474'

response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

soup = BeautifulSoup(html, features="html.parser")

# get all the a tags
# filter the tags for just the urls you want - "showpublisheddocument"
# a_tags = soup.find_all('a')
# <a class="content_link" target="_blank" href="/home/showpublisheddocument/20759/638155516217000000">March 27, 2023</a>

# need dates 
#START HERE
urls_dates = []
for a in soup.find_all('a'):
    if 'showpublisheddocument' in a.get('href', ''):
        urls_dates.append("https://www.greenbeltmd.gov"+a['href'])
        urls_dates.append(a.text)
#print(urls_dates)

#make a list of urls without the dates
urls = []
for a in soup.find_all('a'):
    if 'showpublisheddocument' in a.get('href', ''):
        urls.append("https://www.greenbeltmd.gov"+a['href'])
#print(urls)

#create a container for all the data from the pdfs we're going to parse
#for each url in urls, read the pdf, omitting the column headers
data = []
for url in urls:
    df = tabula.read_pdf(url, pages="all")
    data.append(df)
#print(data)

outfile = open('./reports.csv', 'w')
writer = csv.writer(outfile)
writer.writerows(data)

#now create a single dataframe combining all the dataframes in the data container
#result = pd.concat(data)
        
        
        
        #tabula.convert_into(urls, "output.csv", pages="all")
   

        #for url in urls:
            #tabula.read_pdf(urls, pages="all")
            #tabula.convert_into(urls, "output.csv", pages="all")
            #print("output.csv")

    
        #for urtabula.convert_into(urls_dates)
# the goal is to have a Datasette that shows the most recent weekly crime report, in addition to all the preceding weekly crime reports, say for 2023.
#I think I want a db for each url so we can then put them all together... so that means we want the code that reads the urls and parses the pdfs inside a loop for each url_date


#urls = ['' in a.text and "https://www.greenbeltmd.gov"+a['href'] for a in soup.find_all('a') if 'showpublisheddocument' in a.get('href', '')]

#print(urls)

#for url in urls:
    #read pdf of newest weekly crime report
    #dfs = tabula.read_pdf(url, pages = "all")

    #convert that pdf into a csv file
    #tabula.convert_into(url, "output.csv", pages = "all")

#set up a container for all my records
#list_of_rows = []

        
#broadly speaking, I know this creates a reports.csv file that puts the info from list_of_rows in table form, but I'm not sure what each line does.            
#outfile = open('./reports.csv', 'w')
#writer = csv.writer(outfile)
#writer.writerow(["url", "date"])
#writer.writerows(list_of_rows)








