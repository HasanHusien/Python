# - fetchone => returns a single record or None if no more rows are available.
# - fetchall => fetches all the rows of a query result. It returns all the rows
#               as a list of tuples. An empty list is returned if there is no record to fetch.
# - fetchmany(size) =>

# create file
import sqlite3

db = sqlite3.connect('file.db')
cr = db.cursor()

# create table
cr.execute('create table if not exists users(Id integer, Name text)')

list = ["Ahmed", "Sayed", "Mahmoud", "Ali", "Kamel", "Ibrahim", "Enas"]

# inser data into table
# for key, name in enumerate(list) :
#   cr.execute(f'insert into users(Id, Name) values({key + 1},"{name}")')
  
cr.execute('select * from users')
# cr.execute('select Name from users')


print(cr.fetchone())  # one by one
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchmany(3)) # chose the quantity

print(cr.fetchall())   # all data



# save
db.commit()
# close 
db.close()