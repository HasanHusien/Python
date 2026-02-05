

import sqlite3

dataBase = sqlite3.connect('file.db')
 
cursor = dataBase.cursor() 

# ctreating tables
cursor.execute('create table if not exists students(Id integer, Name text)')

# insert into skills table
list = ["Ahmed", "Sayed", "Mahmoud", "Ali", "Kamel", "Ibrahim", "Enas"]
for index, name in  enumerate(list) :
  cursor.execute(f'insert into students(Id, Name) values({index + 1}, "{name}")') 

# update some data
cursor.execute('update students set name = "hassan" where Id = 1')
cursor.execute('update students set name = "omar" where Id = 2')
cursor.execute('update students set name = "osama" where id = 3')


# delete some data
cursor.execute('delete from students where id = 6')
cursor.execute('delete from students where id = 7')

# save
dataBase.commit()

dataBase.close()









