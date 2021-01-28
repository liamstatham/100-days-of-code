# 100 Days Of Code - Log

### Day 1: Jan 01, Friday

**Today's Progress**: Focusing on continuing to build a foundation in Python using FreeCodeCamp. Begining with: Objects : https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/objects-a-sample-class

**Learnt**:

- Objects
    - Class (A template)
    - Atribute (A variable within a class)
    - Method (A function within a class)
    - Object (A particular instance of a class)
    - Constructor (Code that runs when an object is created)
    - Inheritance (The ability to extend a class to make a new class)

- Where I got too...
    I managed to get to the database part of PY4E during James's nap! Maybe i'll get to do somemore when he has gone to sleep.

    --Update 20:00 pm
    Watched relational database video and installed SQLite, figured out the UI, created a database and used SQL.
    More relational database recap, primary/foreign keys and database design.
    (SQLite data lookup - https://www.py4e.com/lectures3/Pythonlearn-15-Database-Handout.txt)
    Created another relational database with foreign keys as an example.

    Tomorow's starting point: https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/relational-databases-join-operation

**Thoughts**:
I really want to improve my coding, as an expert in SQL with an interest in data I want to be able to manipulate the data in different ways. Potentially with a view to data viz or data analysis. Maybe even to create actual software.
I am struggling with time, due to looking after a toddler.
Finding time late at night is also quite tiring, will be worse when I start work after the Christmas break next week.

Signing off @ 21:30.
------------------------------------------------------------------------

### Day 2: Jan 02, Saturday

### Project Idea:
    - Web scraper to automatically pull details of Forest game stats into a database, which can then be used to create data viz.

**Today's Progress**: Focusing on continuing to build a foundation in Python using FreeCodeCamp. Begining with: yesterdays end point - Relationahl databases. This is more of a recap as I am experienced with databases, SQL and app data.

- Where I got too...
    - Managed to get a quick 30 mins in during James's nap and before Preston V Forest.
    - Further database modelling theory, new SQLite db created with many to many relationships and lookup tables (junction tables).
    - Signing off @ 14:36pm
    - Back online @ 20:20pm (with a dark hot chocolate) ready to do some excersizes.
        - Starting with https://www.youtube.com/watch?v=uQ3Qv1z_Vao
        - Created example db and tested. Fully commented for future eval, uploading to github.
        - Messed around with atom.io trying to link my github account, there's a bug that stops you from connecting to a github project if you already have one open on atom.io!
        - Set up connecton to github db folder and pushed changes.

Examples to follow this evening/later:
    https://www.youtube.com/watch?v=uQ3Qv1z_Vao
    https://www.youtube.com/watch?v=qEkUEAz8j3o
    https://www.youtube.com/watch?v=I-E7avcPeSE
    https://www.youtube.com/watch?v=RZRAoBFIH6A
    https://www.youtube.com/watch?v=xBaJddvJL4A

- Next topic
    - https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/visualizing-data-with-python
    (looking forward to this one).

Thoughts :
Enjoyed learning about SQLite, a little different to T-SQL but still easy to familiarise with. Followed and creatd an example, but fully commented to show understanding and uploaded this to my repo under (DB). Will get used to spending an hour in the evening on coding, hopefully I will be able to wind down after.

Signing off 21:30pm. bonne nuit.
------------------------------------------------------------------------
### Day 3: Jan 03, Sunday

**Today's Progress**: Signed on at 19:15. Continuing the Python & SQLite exercises, starting with https://www.youtube.com/watch?v=qEkUEAz8j3o (creating many to many tables with multiple FKs). Created the exercise and fully noted, uploaded to github DB repo. It parses through a JSON file and inserts the data into 3 different tables in a new SQLite db. Watched the other videos but do not want to use twitter API's and upload my keys to github...
Began watching the dataviz videos, following through the code.
Further reading on d3.js required, looks interesting.
Data viz exercises are here listed beneath this video https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/visualizing-data-with-python

Scientific computing with Python course is now 100% complete! Will need to go back and re-cover the examples. Been a good course. There are some projects to do too.
Signing off 20:30 (had a bad nights sleep last night, so trying to change routine. Hopefully I will be able to continue tomorrow as I am back at work.)
------------------------------------------------------------------------
### Day 4: Jan 04, Monday

**Today's Progress**: Feels like a big day, started my log file searcher project. I've uploaded the start to the master branch under folder "LogFileSearcher". It currently creates a SQLite database, with a relevant table, parses through each relevant line in the file and splits the line into relevant chunks; such as date, time, fromIP, full text etc. It's using the datetime module to convert the date and time strings into a datetime, so I can sort the database by time correctly. Really pleased with the challenges I've overcome today.
Didn't continue the data viz examples as they were a bit boring.

**Issues overcame**: Loop through a file with random line breaks in the wrong place. Count lines correctly, count parts of line correctly. Concat two string parts (year-month-date) and (time:time:time) and then convert to one datetime variable.
------------------------------------------------------------------------
### Day 5: Jan 05, Tuesday

**Today's Progress**: Worked some more on the log search project.
  - Split the lines into correct pieces of information and added each to a variable
  - Converted some to different types for the database
  - Added a SQL script to make sure that no duplicate files will be added to the database, this was a tricky one as there is often nothing specifically different between lines - so ended up using 3 pieces of information to make sure.
  - Added SQL to insert records into table
  - Updated table to reflect relevant information in log file.
  - Tested with a small and full size log file.
  - Also trying to find a new tech blog to read in my downtime.

**Issues overcame**: Finding the time!
------------------------------------------------------------------------
### Day 6: Jan 06, Wednesday

**Today's Progress**: Created another REPO in github to store my projects - 100DoC_Projects.
  - Tidied the code and refactored parts
  - Created a returnvalues function, which returns the next row after being fed the rowid
  - Created a while loop to loop through all rows safely
  - Feel like it's actually clicking.

**Issues overcame**: Nothing, just learning trial and error!

### Day 7: Jan 07, Thursday

**Today's Progress**:
  - Refactored more code, easily loops through rows and exits to next stage when required.
  - Can now export rows to CSV, but trying to get it to export cleanly to xlsx is a bit of a pain.
  - Program is looking better by the day, my knowledge in python3 keeps growing!

### Day 8: Jan 08, Friday

**Today's Progress**:
  - More work on the logfile project
    - removed xlsx stuff, as I fixed the CSV writing to work correctly (and excel on my laptop!)
    - Program now writes to CSV with correct row headers, formatting and no white space. using csvWrite module and newline=''
    - increased speed of adding logs to sqlite database by setting isolation level as deferred (which is like running the whole thing as 1 tran) and turning journal_mode and synchronous off. 34k logs into database took 16mins+ down to 5 mins. Can still get faster, but may have to alter the variables I take from the log.
    - Writes rapidly to CSV.

  **Issues overcame**:
    - Spent a lot of time fine tuning how the program writes to the database to make it more efficient without altering variables.

### Day 9: Jan 09, Saturday

**Today's Progress**:
  - More work on improving data writing to database speed.
    - Removed some variables and left as dict numbers (same data, just more efficient)
    - Removed database initial check and count of current rows as there's no need to do it. Added a drop table if exists and a create table if exists, to make the process more efficient.
    - Reduced time it takes to add 33k log file records to database from 19mins to less than 5 seconds!
    - V1 not far from complete, could add a search and filter down the CSV...
    - Added try/except for file name for safe breaking
    - added search function for URL and printing those results to csv
    - Need to add more try/except for user input sections and then V1 complete.

### Day 10: Jan 10, Sunday

**Today's Progress**:
  - V1.0 of Filesearch.py is complete!
    - Users can't break it with incorrect inputs.
    - Splits log files into human readable format and pushes to a DB quickly.
    - quick search and print results or full db to csv.
    - Simple project, but I've learnt a lot and will be useful for me in a work context.
    - Need to add a file path, as exe can only open files in current directory and I need it to jump up 1 directory.

### Day 11: Jan 11, Monday

**Today's Progress**:
  - V1.0 is actually complete!
    - Just need to document the process.
    - Need to think of the next project now.

  **Issues overcame**:
    - Had to figure out how to find the current directory of the application file, and then use it's parent directory. As in use the application will be nested in it's own folder, in the logs folder. So the application now uses it's parents folder directory. Used both pathlib and os modules to do this.

### Day 12: Jan 12, Tuesday

**Today's Progress**:
  - More updating v1.1 to get it to work with some other log files...
  - More exe work
  - started watching a video on numpi and pandas
  - downloaded 6gb mbox file to start next projects

### Day 13: Jan 13, Wednesday

**Today's Progress**:
  - Started a new project, pulling strava data via API
  - having to learn pandas and figure out json
  - also thought of some more projects...

### Day 14: Jan 14, Thursday

**Today's Progress**:
  - Strava data now pulls correctly to data frames (stravaact.py)
  - data frames are appended and indexing is ignore_index
  - Prints raw data to CSV
  - Using Pandas to transform raw data
    Need to learn much more about pandas.

### Day 15: Jan 15, Friday

**Today's Progress**:
  - Work on the log file project
      - Changed location of CSV file save, now saves to parent directory
      - Changed name of CSV file, now uses log file name
      - Added input() to stop program closing straight away from exe
  - Spend some time working on Strava projects
      - need to learn more about pandas

### Day 16: Jan 16, Saturday

**Today's Progress**:
  - Mainly learning Python pandas and trying examples
  - no project work done, but trying to use real life examples with the pandas learning

### Day 17: Jan 17, Sunday

**Today's Progress**:
  - Using pandas to change and manipulate my csv/dataframe in jupyter notebook
  - A LOT of reading on jupyter/pandas and it's starting to make sense

### Day 18: Jan 18, Monday

**Today's Progress**:
  - I MADE A GRAPH
  - Jupyter notebook and pandas work with my Strava dataviz
  - Continued pandas learning

### Day 19: Jan 19, Tuesday

**Today's Progress**:
  - Loads of progress and learning how to manipulate data in dataframes
  - Learning matplotlib and Pandas
  - creating some graphs with my strava data is really interesting

### Day 20: Jan 20, Wednesday

**Today's Progress**:
  - Progress with seaborn and data viz
  - more data manipulation with pandas
  - more getting used to jupyter as a tool

### Day 21: Jan 21, Thursday

**Today's Progress**:
  - Lots of progress with Pandas and numpy
  - Will write some data manipulations into code when pulling to csv to make it easier to visualise against.

### Day 22: Jan 22, Friday

**Today's Progress**:
  - New project Friday!
  - Began webscraping and learning more HTML/CSS to work with BeautifulSoup
  - Found some real help on FC python, mixing my love of football with coding!

### Day 23: Jan 23, Saturday

**Today's Progress**:
    - More web scraping with BeautifulSoup
    - jupyter and laptop problems causing delays in learning!
    - using transfermarkt website to help with webscraping learning.

### Day 24: Jan 24, Sunday

**Today's Progress**:
    - Moving through the data analysis videos on free code camp
    - more work on web scraping, working on playing with instagram
    - more jupyter learning.

### Day 25: Jan 25, Monday

**Today's Progress**:
  - Continuing through the data analysis lessons on FCC
  - Made a start on the python certification on FCC
      - using the projects to work on

### Day 26: Jan 26, Tuesday

**Today's Progress**:
  - Working on Arithmetic arranger project for FCC cert
  - more list learning, very interesting. Should separate the sums before adding to a list...

### Day 27: Jan 27, Wednesday

**Today's Progress**:
  - Finished the first freecodecamp project, just need to submit it!
  - spent a long time (way longer than the hour on it!)

### Day 28: Jan 28, Thursday

**Today's Progress**:
    - Arithmetic_arranger project should* be done.
    - The project does everything and formats everything as it should, but the replit autograder isn't passing it!
