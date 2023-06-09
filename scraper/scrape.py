from bs4 import BeautifulSoup
import csv
import tabula
import requests
import os
from slack import WebClient
from slack.errors import SlackApiError
import pandas as pd

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
    #putting the rows in the outer container
    list_of_rows.append(each_row)
#list_of_rows = []

outfile = open('./reports.csv', 'w')
writer = csv.writer(outfile)
writer.writerow(["url", "date"])
writer.writerows(list_of_rows)

#read pdf of newest weekly crime report
tables = tabula.read_pdf(list_of_rows[0][0], pages = "all")
latest_df = [pd.DataFrame(tables) for table in tables]
print(latest_df)
#convert that pdf into a csv file
#tabula.convert_into(list_of_rows[0][0], "output.csv", pages = "all")


#slack_token = os.environ.get('SLACK_API_TOKEN')
#client = WebClient(token=slack_token)

#msg = "Greenbelt PD CrimeBot here. See https://www.greenbeltmd.gov/government/departments-con-t/police/crime-reports/weekly-crime-report/-folder-1474"
#try:
    #response = client.chat_postMessage(
        #channel="slack-bots",
        #text=msg,
        #unfurl_links=True, 
        #unfurl_media=True
    #)
    #print("success!")
#except SlackApiError as e:
    #assert e.response["ok"] is False
    #assert e.response["error"]
    #print(f"Got an error: {e.response['error']}")


