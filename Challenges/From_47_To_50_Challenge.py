# [1]

number = int(input('Whats The Number ? '))

while number > 0 :
  
  number -= 1
  
  if number == 6 :
    continue
  
  elif number == 0 :
    break
  
  print(f'Number: {number}')
  
  if number == 1 :
    print("8 Numbers Printed Successfully.")
  
else :
  print ("Number 0 Is Not Larger Than 0")  
    
# # Needed Output
# 9
# 8
# 7
# 5
# 4
# 3
# 2
# 1
# "8 Numbers Printed Successfully."

# [2]

friends = []
count = 4


while len(friends) < 4 :
  
  name = input('whats your name ? ')
  
  if name.isupper() :
    print('Invalid Name')  
    
    
  elif name[0].isupper() :
    count -= 1
    print(f"Friend {name} Added")
    print(f"Names Left in List Is {count}") 
    friends.append(name)
    
  elif name.islower() :
    count -= 1
    print(f'Friend {name} Added => 1st Letter Become Capital')
    print(f"Names Left in List Is {count}")
    friends.append(name)
    
else :
  print(friends)    
    
    
 
