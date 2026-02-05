
# Databace [connect] [create] [close]

# import sql lite
import sqlite3

# make database file
db = sqlite3.connect('app.db')

# put data in file
db.execute('create table if not exists skills(id integer, name text, quantitiy integer)')

# clode file
db.close()