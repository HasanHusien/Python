# [1]

def get_score(**data) :
  for key, value in data.items() :
    print(f'{key} => {value}')

# Tests
get_score(Math=90, Science=80, Language=70)
get_score(Logic=70, Problems=60)
# Output
"Logic => 70"
"Problems => 60"
"Math => 90"
"Science => 80"
"Language => 70"

# [2]

def get_people_scores(*name, **score) :
  if name and score:
    #[0] for remove (...,) form tuple
    print (f"Hello {name[0]} This Is Your Score Table:") 
    
    for key, value in score.items():
      print(f'{key} => {value}')
      
  else :
    if name != True  and score:
      
      for key, value in score.items():
        print(f'{key} => {value}')
        
    if score != True and name:
      
      print(f"Hello {name[0]} You Have No Scores To Show")    
  
  
  
  
# Test 1
get_people_scores(str("Osama"), Math=90, Science=80, Language=70)

# Output
"Hello Osama This Is Your Score Table:"
"Math => 90"
"Science => 80"
"Language => 70"

# Test 2
get_people_scores("Mahmoud", Logic=70, Problems=60)

# Output
"Hello Mahmoud This Is Your Score Table:"
"Logic => 70"
"Problems => 60"

# Test 3
get_people_scores(Logic=70, Problems=60)

# Output
"Logic => 70"
"Problems => 60"

# Test 4
get_people_scores("Ahmed")

# Output
"Hello Ahmed You Have No Scores To Show"





