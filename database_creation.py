import sqlite3

database = sqlite3.connect("database.db")
cur = databse.cursor()
###### variable declaring and assignment ##########

s_no = input("serial number")
name = input("name")
batch = input("batch")
des = input("description")

####### table creation ############

table = ''' CREATE TABLE IF NOT EXISTS notes(s_no INTEGER PRIMARY KEY,name TEXT,batch TEXT,description TEXT);'''
cur.execute(table)
