# [3]

# Input
my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}
degree ={
  'A' : 100,
  "B" : 80,
  'C': 40
}
def degree(value) :
  if value == "A" :
    return 100
  elif value == 'B' :
    return 80
  elif value == 'C' :
    return 40
  elif value == 'D' :
    return 20
  
  
for key, value in my_ranks.items() :
    print(f"My Rank in {key} Is {value} And This Equal {degree(value)} Points")
else :
  print("Total Points Is 320")
# Needed Output
"My Rank in Math Is A And This Equal 100 Points"
"My Rank in Science Is B And This Equal 80 Points"
"My Rank in Drawing Is A And This Equal 100 Points"
"My Rank in Sports Is C And This Equal 40 Points"
"Total Points Is 320"

print('#' * 20)

# Input
students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}

for student_key , student_value in students.items() :
  
  print(f" Student Name => {student_key}")  
  
  for subject_key, subject_value in student_value.items():
    
    print(f"{subject_key} => {degree(subject_value)} Points")

# Another Way
for student in students :
  print(f"Student Name => {student}")
  
  for sub_keym, sub_val in students[student].items() :
    
   print(f"{sub_keym} => {degree(sub_val)} Points")
  
  
  

# Needed Output
"------------------------------"
"-- Student Name => Ahmed"
"------------------------------"
"- Math => 100 Points"
"- Science => 20 Points"
"- Draw => 80 Points"
"- Sports => 40 Points"
"- Thinking => 100 Points"
"Total Points For Ahmed Is 340"
"------------------------------"
"-- Student Name => Sayed"
"------------------------------"
"- Math => 80 Points"
"- Science => 80 Points"
"- Draw => 80 Points"
"- Sports => 20 Points"
"- Thinking => 100 Points"
"Total Points For Sayed Is 360"
"------------------------------"
"-- Student Name => Mahmoud"
"------------------------------"
"- Math => 20 Points"
"- Science => 100 Points"
"- Draw => 100 Points"
"- Sports => 80 Points"
"- Thinking => 80 Points"
"Total Points For Mahmoud Is 380"

