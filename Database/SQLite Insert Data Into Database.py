# -- Databases => SQLite => Insert Data Into Database --
# - cursor => All Operation in SQL Done By Cursor Not The Connection Itself
# - commit => Save All Changes

import sqlite3

dataBase = sqlite3.connect('app.db')
 
cursor = dataBase.cursor() 

# ctreating tables
cursor.execute('create table if not exists skills(id integer, name text)')
cursor.execute('create table if not exists students(id integer, name text, degree integer)')


# insert into skills table
my_list = ["Ahmed", "Sayed", "Mahmoud", "Ali", "Kamel", "Ibrahim", "Enas"]
for index, name in  enumerate(my_list) :
  cursor.execute(f'insert into skills(id, name) values({index + 1}, "{name}")')
  
  
# insert data in students table
cursor.execute('insert into students(id, name, degree) values(1, "Hassan", 99)')
cursor.execute('insert into students(id, name, degree) values(2, "Ahmed", 87)')
cursor.execute('insert into students(id, name, degree) values(3, "omar", 98)')

   

# save
dataBase.commit()

dataBase.close()









