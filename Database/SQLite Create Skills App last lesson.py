import sqlite3 

db = sqlite3.connect('data.db')

cr = db.cursor()

userId = 4

# save and close function
def saveCloe() :
  
  db.commit()
  
  db.close
  
  print('data base closed succusfly')

# create table 
cr.execute('create table if not exists skills(name text, progress integer, userId integer)')  

# Input Message
inputMessage = """
What Do You Want To Do ?
"s" => Show All Skills
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
Choose Option:
"""
correctInputs = ['a','s','d','q','u']

commands = input(inputMessage).strip().lower()


def show_skills():
  
  cr.execute('select * from skills')
  
  print(cr.fetchall())
  
  print('data showed successfully')

  saveCloe()

def add_skill():
  
  skill = input('please write your skill: ')
  
  progress = input('please write your progress: ')
  
  cr.execute(f"insert into skills(name, progress, userId) values('{skill}', '{progress}', '{userId}')")
  
  print('Data Adedd successfully')

  saveCloe()
 
def delete_skill():
  
  skill = input('please write your skill: ')
  
  userId = input('please write userId: ')
  
  cr.execute(f"delete from skills  where name = '{skill}' and userId = '{userId}'")

  print("Skill deleted successfully")
  
  saveCloe()

def update_skill():
  
  newSkill = input('please write the new skill: ')
  
  userId = input('please write userId: ')
  
  cr.execute(f'update skills set name = "{newSkill}" where userId = "{userId}"')
  
  print('data updating successfully')

  saveCloe()

if commands in correctInputs :
  # print(f'yes this commind is hire {commands} wondurful !')
  
  if commands == 's' :
    show_skills()
    
  elif commands == 'a' :
    add_skill()
    
  elif commands == 'u' :
    update_skill()
    
  elif commands == 'd' :
    delete_skill()
    
  else :
    print('quit')
    
else :
  print('sorry this commands is not found')  


