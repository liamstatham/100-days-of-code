import sqlite3
from datetime import datetime
#Create sqlite database
#conn = sqlite3.connect('logdb.sqlite')
#cur = conn.cursor()

#Create logs table
#cur.execute('''
#CREATE TABLE if not exists Logs (
#    LogID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#    FromFile TEXT,
#    Datetime DATETIME,
#    FromIP TEXT,
#    FullText TEXT
#); ''')

#Open file
fname = input('Enter file name: ')
if len(fname) < 1: fname = 'u_ex210102.log'
file = open(fname)

records = 0
for lines in file:
    if not lines.startswith('2021'):continue
    line = lines.split()
#need to convert line[0] and line[1] from string to datetime
    bigdate = line[0]
    time = line[1]
    fulldate = (bigdate + ' ' + time)
    dt = datetime.fromisoformat(fulldate)
#Above converts part 0 and 1 from log file line to a full date. using datetime 
#    print(type(line[1]))
    print(dt)
    records = records + 1
print('Number of records to enter into database: ',records)
#splits file into lines beginging with 2021


#print(counts)
