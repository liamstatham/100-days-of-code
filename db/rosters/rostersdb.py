import json
import sqlite3
#IMports json and sqlite3
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')
#user input file name
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data_sample.json'
    #defaults to above file if length of input is less than 1
    #json file is just an array of data

str_data = open(fname).read()
json_data = json.loads(str_data)
#Opem json file

for entry in json_data:

    name = entry[0];
    title = entry[1];

    print((name, title))
    #creates an array of the data in json file so we can parse it

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    #Inserts name into created User table, if the name IS unique or it gets ignored
    #? placeholder is to avoid sql injection and uses the (name,)) variable
    # adds the created rowID to the user_id variable to store

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]
    #inserts title into Course TABLE
    # adds the created rowid to the course_id variable to store

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id) VALUES ( ?, ? )''',
        ( user_id, course_id ) )
    #inserts the stored rowid's in the variables user_id and course_id into the Member table

    conn.commit()
