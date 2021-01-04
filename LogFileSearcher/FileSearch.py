import sqlite3
import datetime
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
#    dt = datetime.datetime(line[0])
#    tm = datetime.time(line[1])
#    combine = datetime.combine(dt, tm)
    print(line[0], line[1], combine)
    records = records + 1
print('Number of records to enter into database: ',records)
#splits file into lines beginging with 2021


#print(counts)
