from bs4 import BeautifulSoup
import csv
import tabula
import sqlite_utils
import datasette_codespaces
import requests
import os
from slack import WebClient
from slack.errors import SlackApiError
import datetime
from datetime import date, timedelta, datetime
import pandas as pd

url = 'https://www.greenbeltmd.gov/i-want-to/view/weekly-crime-report/-folder-1474'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

soup = BeautifulSoup(html, features="html.parser")
ul = soup.find_all('ul')[-1]

#inside the loop, create an empty dictionary: dict = {} and populate it with each url and date. Then append dict to your urls_with_dates

#set up a container for all my records (my list of dictionaries)
urls_with_dates = []
#start my loop
for li in ul.find_all('li'):
    #find the a tags, which is where the info is
    for a in li.find_all('a'):
        #set up a container for my dictionaries, which will include the dates and urls to put in my urls_and_dates container
        dict={}
        #in each a tag, find the href and add it to the basic Greenbelt government website url to get the url of the weekly crime report, and define that as a url
        #in each a tag, find the text and define that as a date
        if li.find('a'):
            dict['url'] = "https://www.greenbeltmd.gov" + li.find('a')['href']
            dict['date'] = a.get_text()
        #print(dict)
    urls_with_dates.append(dict)
#print(urls_with_dates)

#isolate the date of the latest report and convert it into Y-M-D format
latest_report = urls_with_dates[0]['date']
date_obj = datetime.strptime(latest_report, "%B %d, %Y")
formatted_latest_report = date_obj.strftime("%Y-%m-%d")
#print(formatted_latest_report)

#set today and yesterday so I can check the date of the latest report against the most recent Monday (which is when I would expect a new report to be posted)
today = date.today()
yesterday = today - timedelta(days=1)
#print(today)
#print(yesterday)

#I'll use the below when I serve the complete scraped reports in Datasette.
#For each dictionary (url-date pair), create a dataframe containing the contents that result from reading each pdf.
#all_reports = []
#for each in urls_with_dates:
    #table = tabula.read_pdf(each['url'], pages="all")
    #tabula.convert_into(each['url'], "all_reports.csv", pages="all")
    #print(all_reports)

#Parse the pdf for the most recent report, make it into a csv, and count the number of rows (incidents).
most_recent = tabula.read_pdf(urls_with_dates[0]['url'], pages="all")
tabula.convert_into(urls_with_dates[0]['url'], "latest_report.csv", pages="all")
with open('latest_report.csv', 'r') as file:
    reader = csv.DictReader(file2)
    weekly_incidents = sum(1 for row in reader)
    #print(weekly_incidents)


slack_token = os.environ.get('SLACK_API_TOKEN')
client = WebClient(token=slack_token)

msg = "Greenbelt PD CrimeBot here. "
if formatted_latest_report != yesterday:
    msg += (f"There's a new weekly crime report for the week ending {formatted_latest_report}. The Greenbelt PD reported {weekly_incidents} incidents for <{urls_with_dates[0]['url']}|that week>.\n")
elif formatted_latest_report == yesterday:
    msg += ("No new report for now!")

try:
    response = client.chat_postMessage(
        channel="slack-bots",
        text=msg,
        unfurl_links=True, 
        unfurl_media=True
    )
    print("success!")
except SlackApiError as e:
    assert e.response["ok"] is False
    assert e.response["error"]
    print(f"Got an error: {e.response['error']}")
