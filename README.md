# steph_gpd_bot
This bot will help me to harvest and analyze weekly crime data from the Greenbelt Police Department in Greenbelt, MD.

April 1 turn-in:
What I started with this week was a Python script that used Beautiful Soup to identify the final <ul> tag on the webpage listing Greenbelt Police Department weekly crime reports, drill down into that <ul> to iterate over each <a> tag corresponding to an individual report, and use the contents of those <a> tags to create a table listing the url for each report and its corresponding date. 

In order to get a better understanding of the workflow for my bot, I started this week by revising my scrape.py file to target the url of the most recent GPD weekly crime report in the Python object I created last week and parse that pdf using Tabula-py. I needed to create a second bash file to use SQLite-utils to create a SQLite database containing the content of only that pdf and then get Datasette to serve the .db file. 

I had a lot of trouble figuring out how to move beyond the above to get my code to scrape and parse *all* the pdfs on the GPD weekly crime report webpage, but I think I more or less did it!  For some reason, I started by redoing a lot of the work I did last week, except filtering all the many <a> tags on the page for those that contained "showpublisheddocument" in the href. I realized that it would be easier to build off of the version of my scraper that I already had. But I still had to figure out how to get Tabula-py to loop through each url in the unordered list containing my pdfs, and I wanted to keep a version of my table with both the urls and the dates. I ended up starting a new scrape2.py file because the old one felt like too much of a muddle.

Inside the loop that I wrote last week, I created a list of dictionaries matching my urls and dates and identifying them as such. I put this list of dictionaries in a container called urls_and_dates.

Then, to work toward the database with all the records from 2023, I wrote Python code so that Tabula-py would parse the pdf in each url in urls_and_dates and write that information to a csv file.

Finally I used a similar bash file to the one I wrote last week to create a SQLite database containing contents of all the urls and serve up that information in Datasette.

Still to do:
Automate the above workflow using GitHub Actions. I'm not exactly sure how to do this yet, but I think I will need to adjust the YAML file from the class Git-scraping assignment to fit my purposes. I will also need to figure out exactly what schedule I want my bot to operate on. I think GPD adds the latest report every Monday or so, so maybe my bot can work Tuesdays at  midnight?

And I need to figure out how to get my bot to send me a Slack message (or email?) when there's new info. 

I think the above is probably doable for this week. If I have extra time I could try and add some canned SQL queries to run each time on the data.
