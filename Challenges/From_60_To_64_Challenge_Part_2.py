
scores_list = {
"Math" : 90,
"Science" : 80,
"Language" : 70,
}

def get_the_scores(*name, **list) :
  
  if name and list :
    print(f"Hello {name[0]} This Is Your Score Table:")  # [0] couse tuple
      
    for key, value in list.items() :
      print(f'{key} => {value}')
      
  else :
    if name != True and list:
      
      for key, value in list.items() :
        print(f'{key} => {value}')
        
    if list != True and name :
       print(f"Hello {name[0]} You Have No Scores To Show")
        
  
# Test 1
get_the_scores("Osama", **scores_list)

# Output
"Hello Osama This Is Your Score Table:"
"Math => 90"
"Science => 80"
"Language => 70"

# Test 2
get_the_scores("Osama")

# Output
"Hello Osama You Have No Scores To Show"

# Test 3
get_the_scores(**scores_list)

# Output
"Math => 90"
"Science => 80"
"Language => 70"