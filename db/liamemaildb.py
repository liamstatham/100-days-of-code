import sqlite3
#import sqlite3 and create a new database and open a cursor
conn = sqlite3.connect('liamemaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
#Drops table if table already exists

cur.execute('CREATE TABLE Counts (Email TEXT, Count INTEGER)')
#Creates new table for counting email addresses in file

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
#User to enter a file name, if enter is pressed with no input it defaults to mbox-short.txt (from example)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    #Lines starting with "From: " are split into words, in example the 2nd word is the email address, so we use the 2nd piece of pieces
    cur.execute('SELECT Count from Counts WHERE Email = ? ', (email,))
    #Use ? place holder and then a tuple variable to prevent sql injection
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (Email, Count) VALUES (?, 1)''', (email,))
        #Uses the email piece from pieces from the line in file as the variable for ? in the tuple (email,)
    else:
        cur.execute('UPDATE Counts SET Count = Count + 1 WHERE Email = ?', (email,))
        #if email already exists, add 1 to the count
    conn.commit()

sqlstr = 'SELECT Email, Count FROM Counts ORDER BY Count DESC LIMIT 10'
#Quick select statement to print in terminal
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
    #Prints out the select statement - converts first row to string (as it's the email), 2nd row is count

cur.close()
#Close cursor
#test code update for git pushing.
