# Input
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]

i = 0
lostNames = 0

while i <= len(friends) - 1 :
  

  if friends[i].islower() == False :  # if it not lower char get word
    
    print(friends[i])
    
  else :
    lostNames += 1  
    
  i += 1 
  
else :
  print(f'"Friends Printed And Ignored Names Count Is {lostNames}"')
  
# # Needed Output
# "Mohamed"
# "Shady"
# "Sherif"
# "Friends Printed And Ignored Names Count Is 2"


# [2]

# Code
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]


while skills:
  
  print(skills.pop(0))   # smart one its damn!
  # Type The Code Here in One Line

# Needed Output
"HTML"
"CSS"
"JavaScript"
"PHP"
"Python"
