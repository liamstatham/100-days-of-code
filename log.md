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

### Day 29: Jan 29, Friday

**Today's Progress**:
  - Finished the Arithmetic_arranger project and passed the freecodecamp first project!
  - Started 2nd project for certification: Time_Calculator which seems quite tough

### Day 30: Jan 30, Saturday

**Today's Progress**:
  - Finished the Time_Calculator project on freecodecamp
  - learnt a lot about datetime and time modules

### Day 31: Jan 31, Sunday

**Today's Progress**:
  - Made a start on the Budget App project
  - Mostly done, learnt a lot about Classes, functions and unit testing


### Day 32: Feb 1, Monday

**Today's Progress**:
  - Continued work on the budget app
  - Lots of class/function work
  - Very interesting

### Day 33: Feb 2, Tuesday

**Today's Progress**:
  - James is 2 today! So had to fit it in around his nap time!
  - Did a bit more work on the budget app, all functions are now in the class
  - need to start the other function out of the class "create spend chart"
  - had a quick look, looks very difficult and I need a fresh head to start this one.

### Day 34: Feb 3, Wednesday

**Today's Progress**:
  - Not a good day, not well!
  - struggling to get my head around the weird text chart output

### Day 35: Feb 4, Thursday

**Today's Progress**:
  - Finished the budget app, had to fudge it though as I'm sure the auto grader is broken!
  - Made a start on the 4th Project of the cert. Polygon area calculator.
  - Looks quite fun.

### Day 36: Feb 5, Friday

**Today's Progress**:
  - Finished the Polygon area calculator, spent way more than an hour on it today, but smashed it!
  - 1 more project to complete until certification!
  - https://repl.it/@LiamStatham/boilerplate-polygon-area-calculator-1

### Day 37: Feb 6, Saturday

**Today's progress**:
  - Finished the certification!
  - Final project was a probability calculator, needed help with the maths but the code was fine!

### Day 38: Feb 7, Sunday

**Today's progress**:
  - Made a start on web design/front end. Think this is where I want to head.
  - Refreshed knowledge on HTML/HTML5, breezed through it in around 2 hours.

### Day 39: Feb 8, Monday

**Today's progress**:
  - Taking a dive into javascript
  - Spoke to some devs at work, advised that things are moving towards javascript and it's probably good to learn.
  - Started the course on fcc!

### Day 40: Feb 9, Tuesday

**Today's progress**:
  - More javascript, done a fair bit of catching up with the syntax changes from python
  - did a lot of reading javascript wise

### Day 41: Feb 10, Wednesday

**Today's progress**:
  - Even more javascript, makes sense, seems way more flexible than python
  - made a little card counting script
  - learnt about js objects and calling/changing them
  - Spent more than an hour, 80% through the course though!

### Day 42: Feb 11, Thursday

**Today's progress**:
  - More JavaScript!
  - Learnt about modifying JSON objects using my own functions
  - Made contact with the dev manager at work to see what's best to learn for an opportunity...

### Day 43: Feb 12, Friday

**Today's progress**:
  - Started on C# syntax, this is where my pathway into a job is
  - Signed up to pluralsight, and started the c# fundamentals videos and projects
  - https://app.pluralsight.com/course-player?clipId=3f7b7f5e-8a98-418c-8733-45ebdfcf094c

### Day 44: Feb 13, Saturday

**Today's progress**:
  - Busy day today, but still managed to squeeze in an hour of C#
  - Enjoying the work along stuff with pluralsight, where you have to figure out what to do before the answer is provided.
  - https://app.pluralsight.com/course-player?clipId=1acccfd3-3a64-4719-9bbb-8dc3a43b1c64

### Day 45: Feb 14, Sunday

**Today's progress**:
  - Loads more C#, good few hours, learnt more syntax, code encapsulation, classes, objects, methods etc!
  - Loving it.
  - https://app.pluralsight.com/course-player?clipId=54eb1aab-f19e-4828-b4cd-761873608479

### Day 46: Feb 15, Monday

**Today's progress**:
  - https://app.pluralsight.com/course-player?clipId=da67bd8b-7dec-4347-ab62-da09aa2dc70f
  - More C# and an intro into unit testing with Xunit
  - Code refactoring

### Day 47: Feb 16, Tuesday

**Today's progress**:
  - Reference types vs value types
  - more unit testing
  - More C#!
  - https://app.pluralsight.com/course-player?clipId=1428326e-49f9-4067-a655-900c87d8253d

### Day 48: Feb 17, Wednesday

**Today's progress**:
  - if statements
  - for, for each, do while and while loops
  - flow of execution
  - unit testing!
  - very busy day at work and no time this evening, so struggled!
  - https://app.pluralsight.com/course-player?clipId=83f514dd-e6e8-441e-a9e7-19243615ddbd

### Day 49: Feb 18, Thursday

**Today's progress**:
  - C# loops, jumping statements (break, continue)
  - Pattern matching with switch statements
  - Try Catch exception handling
  - https://app.pluralsight.com/course-player?clipId=36877d9c-72dd-4c46-a883-8538f5de1c54

### Day 50: Feb 19, Friday

**Today's progress**:
  - Started working on a new logfile project in C#
  - Lots to learn!
  - Defining properties etc!
  - https://app.pluralsight.com/course-player?clipId=36bbca95-96bb-4e5b-8efd-4bb324e68d85

### Day 51: Feb 20, Saturday

**Today's progress**:
  - Made a lot of progress on my c# project
  - splitting a lot of code into methods/classes

### Day 52: Feb 21, Sunday

**Today's progress**:
  - More work on the log file app in C#
  - Had to create a new project in VS, rather than VS code.
  - Learnt more about methods/Classes
  - Found the dataframes nuget, looks very similar to python
  - Need to continue the videos on pluralsight whilst working on the projects.

### Day 53: Feb 22, Monday

**Today's progress**:
  - More log file work!
  - Figured out how to split lines into words safely, into a string array
  - Broke everything down into smaller methods
  - Need to learn about data tables or data frames and then into a database, or just a CSV from data.

### Day 54: Feb 23, Tuesday

**Today's progress**:
    - More log file work!
    - New Class for sqlite stuff
    - Another method to pass a name to new database ?
    - SQLite work, but need to get data from intodatatable method to table!

### Day 55: Feb 24, Wednesday

**Today's progress**:
  - Some pluralsight videos
  - Learn about c# delegates and events
  - Made a start on OOP module
  - Deriving from base classes  

### Day 56: Feb 25, Thursday

**Today's progress**:
  - Abstract Classes/polymorphism
  - Interface definition
  - Refactoring and encapsulation!
  - Finished the C# fundamentals video course

### Day 57: Feb 26, Friday

**Today's progress**:
    - Using File to check for/create new csv file with logfile fname
    - using a new method to create that csv
    - using another method to write to it
    - https://stackoverflow.com/questions/18757097/writing-data-into-csv-file-in-c-sharp

### Day 58: Feb 27, Saturday

**Today's progress**:
  - Big progress on c# project
  - log file is now writing heading and logs to csv correctly
  - more refactoring needed, but works!
  - need to parse datetime and make it work with a real log file.

### Day 59: Feb 28, Sunday

**Today's progress**:
  - Refactoring and added saftey measures to the log file parse
  - can now parse any of works log files, only uses lines which start with a number
  - less than 30 seconds to put a full log file into csv

### Day 60: March 01, Monday

**Today's progress**:
    - Difficult and long day at work today, but still ground over an hour out!
    - Added Xunit unit testing and 2 simple file name tests to my project
    - Took a while to figure out, but it's all learning at the end of the day!

### Day 61: March 02, Tuesday

**Today's progress**:
  - More unit testing and Refactoring
  - Tomorrow, should break creating headings in csv file into a new method and create tests for it
  - Enjoying going over my code and making it more safe!

### Day 62: March 03, Wednesday

**Today's progress**:
  - More unit testing and Refactoring
  - Enhancing usability of the app
  - Started to create SQL class and ability to for user choice

### Day 63: March 04, Thursday

**Today's progress**:
  - Tried SQLite but DataTables seem a lot more valid for my Program
  - spent time adding a new data table class, with methods and calling from my Program

### Day 64: March 05, Friday

**Today's progress**:
  - Datatable work and program improvement
  - Changed the contents that are pulled from log files
  - created method to add data to tables from program

### Day 65: March 06, Saturday

**Today's progress**:
  - Got datatables working, but in one big class which needs Refactoring
  - need to add search/filtering/then to csv
  - Potentially make it more efficient...

### Day 66: March 07, Sunday

**Today's progress**:
  - Added methods to filter data tables
  - Added extra steps in main program, more usability
  - a bit more testing...

### Day 67: March 08, Monday

**Today's progress**:
  -https://app.pluralsight.com/course-player?clipId=1c51f836-d151-4708-8452-345d6daa9855
  - Started learning asp.net core, hopefully building a web app

  - but started learning MVC as it's more relevant to work instead.

### Day 68: March 09, Tuesday

**Today's progress**:
  - Long day at work 11 hours
  - Still managed an hour of ASP.NET MVC Learning
  - Separation of duties for the Model view and controller

### Day 69: March 10, Wednesday

**Today's progress**:
  - More MVC learning
  - Application start and configuration (notes)
  - more emphasis on separation of duties

### Day 70: March 13, Saturday

**Today's progress**:
  - MVC controllers
  - API controllers and how HTTP controllers work with Examples

### Day 71: March 14, Sunday

**Today's progress**:  
  - More MVC controller work
  - API controller and building api

### Day 72: March 15, Monday

**Today's progress**:  
  - More Controller learning
  - Some work on models
  - Learning about Enums

### Day 73: March 16, Tuesday

**Today's progress**:  
  - MVC models in depth
  - Data annotations for data validation
  - model binding
  - GET/POST work.

### Day 74: March 17, Wednesday

**Today's progress**:
  - MVC actions/redirects
  - Updating records using GET/POST actions in the controller/services
  - An intro into Entity Framework

### Day 75: March 18, Thursday

**Today's progress**:
  - c# clean code fundamentals videos
  - Entity framework and setting up databases
  - entity framework for GET/POST requests

### Day 76: March 19, Friday

**Today's progress**:
  - Made a quick MVC website with in memory data for toy car auditing
  - nice to do it without following a tutorial!
  - Will need to keep doing it.

### Day 77: March 20, Saturday

**Today's progress**:
  - Added some improvements
  - Need to make the in memory database work!
  - Very interesting

### Day 78: March 21, Sunday

**Today's progress**:
  - Added in memory database, along with add and edit control
  - Really enjoying it!
  - The issue was it needed to use SingleInstance (singleton)

### Day 79: March 22, Monday

**Today's progress**:
  - Added a SQL database to Jims Cars
  - Can now Add, edit, view and delete into the database
  - Also watched another pluralsight video
  - Tomorrow I need to learn about styling!

### Day 80: March 23, Tuesday

**Today's progress**:
  - Work on Razor Views and how to use
    - partial Views
    - layout Views
    - @model stuff and alerts effectively
  - jquery validation

### Day 81: March 24, Wednesday

**Today's progress**:
  - Finished the ASP.NET MVC course on pluralsight
  - Learned how to deploy MVC websites to IIS via filesystem
  - Learned a bit about IIS and local SQL server instances

### Day 82: March 25, Thursday

**Today's progress**:
  - Started another course on Collections in c#
  - I know most of it, but want to make sure I know it al
  - did a few experiments

### Day 83: March 26, Friday

**Today's progress**:
  - Started the project test on C# fundamentals pluralsight
  - 54% of the way through, need to learn a bit more linq!
  - really need to learn some bootstrap, I think I prefer web dev.

### Day 84: March 27, Saturday

**Today's progress**:
  - Started on learning bootstrap/css/js/angular on a cool new course
  - sticking with asp net core for web apps
  - new project - dutch treat?

### Day 85: March 28, Sunday

**Today's progress**:
  - A big look into HTML
  - Serving static files via webservers

### Day 86: March 29, Monday

**Today's progress**:
  - CSS learning (yes actual style!)
  - decent notes and examples on this in one notes

### Day 87: March 30, Tuesday

**Today's progress**:
  - Lots of Azure work fundamentals/dev ops
  - an intro into JS and some code 

Liam Statham
