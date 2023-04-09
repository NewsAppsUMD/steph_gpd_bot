# steph_gpd_bot
This bot will help me to harvest and analyze weekly crime data from the Greenbelt Police Department in Greenbelt, MD.

April 8 (final) turn-in: 

My big initial win was getting my bot to scrape the Greenbelt PD's website to (1) create a table containing urls of all available weekly crime reports from 2023 with their corresponding dates, (2) use Tabula-py to parse the pdf for the most recent report and convert it into a csv and (3) use sqlite-utils to create a database file that could then be served as a searchable version of the report in Datasette. 

Then I had to figure out how to get Tabula-py to loop through each url and parse all the pdfs without overwriting the previous ones. Inside the loop that I wrote the previous week, I created a list of dictionaries matching my urls and dates and identifying them as such and put this list of dictionaries in a container called urls_with_dates. I used Tabula-py to parse the url in each dictionary/row and amass all the records into a csv.

The next tasks were to get my bot to automatically scrape on a schedule and send me Slack updates after it ran. I tailored my yaml file to scrape the Greenbelt PD website on Tuesdays at 2 a.m. EST, since new weekly crime reports seem to be posted on Mondays. After setting up my SlackBot, I coded it to tell me whether or not a new weekly crime report has been posted (though see the caveat below) and, in cases where there is a new report, to say how many incidents were listed in the report and give a link to the new report. 

What I wanted it to do that it doesn't do:
1. Right now, my bot's ability to tell me if the latest weekly crime report is new or not is dependent on the bot running only on Tuesdays, because I'm checking the date of the most recent available report against "yesterday." This assumes that the Greenbelt PD only posts new reports on Mondays (which I think is usually true) and does not gauge the newness of the most recent report by checking it against the last report the bot scraped. I'm not sure how to do the latter, but I'll work on that moving forward.

2. I tried for this turn-in to get my Slack message to say how many incidents the Greenbelt PD had reported in all of 2023, as well as how many it reported in the most recent weekly crime report. Since I had trouble converting what I parsed in Tabula into Pandas dataframes, this would have required me to create a csv file with the contents of all the weekly crime reports and to count the rows. I managed to create an object called all_reports that contains all this information, but I couldn't figure out how to make it a single csv. (I thought I had done this before, but maybe I never had the csv for all the data?)

3. I can't rely on GitHub Actions to run my Datasette because Actions can't sustain a server, so right now I have to run my sqlite_command.sh file manually to use the Datasette function of my bot. This isn't necessarily a big deal, but I had hoped to run some canned SQL queries on the amalgamated data and had originally envisioned Datasette as the way to do this. This is something else for me to work on moving forward.

4. Ideally, the bot would add a csv of the latest weekly crime report to my repository each time a new report appeared. It's not clear to me that my bot does this as it stands, although I originally thought the "commit and push if it changed" job in my yaml file would do this. Was I misunderstanding?

5. I don't seem to be getting a Slack message when I run my bot by pushing to my repo. Why not?

General reflections:
I'm disappointed that my bot doesn't do everything I wanted it to do, but I also feel as though I've gained skills every week and come a long way since the beginning. I think the technical aspects of building this bot were challenging enough for me that I didn't pay as much attention to more journalistic concerns as I would have liked. As I move forward with my final project, I hope to be more guided by potential journalistic uses of my bot and the app I will build from it.

--

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
