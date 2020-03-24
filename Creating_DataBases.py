#Create a table abc and insert records of name and number using databases in Python
import sqlite3
conn=sqlite3.connect('NewDB.sqlite')
curr=conn.cursor()

curr.execute('DROP TABLE if EXISTS abc')
curr.execute('CREATE TABLE abc(NAME VARCHAR,NO INTEGER)')
while 1:
    name=input("Enter Name")
    no=input("Enter Number")
    curr.execute('INSERT INTO abc(NAME,NO) VALUES (?,?)',(name,no))
    while 1:
        ch=input("Do you want to add more?")
        if ch=='yes':
            break
        elif ch=='no':
            break
        else:
            print("Invalid choice")
    if ch=='no':
        break
curr.execute('SELECT * from abc')
a=curr.fetchall()
for row in a:
    print('Name:',row[0],'Number:',row[1])