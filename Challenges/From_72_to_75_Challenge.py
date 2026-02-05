# [1]
friendsNams = ["AEmanS", "AAhmedS", "DSamehF", "LHassanL"]

def removeChar(name) :
  return name[1:-1]

cleanNames = map(removeChar, friendsNams)

for name in cleanNames :
  print(name)

# or
noneNameFunction = lambda name : name[1:-1]

cleanNamesWithMap = map(noneNameFunction, friendsNams)

for name in cleanNamesWithMap :
  print(name)

# Output
"Eman"
"Ahmed"
"Sameh"
"Hassan"

print('*' * 25 )

# [2]

friends_filter = ["Hassan", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

def getNameWithM(name) :
  return name.endswith('m')

NamesWithM = filter(getNameWithM, friends_filter)

for name in NamesWithM :
  print(name)
  

# or 

for name in  filter(lambda name : name.endswith('m'), friends_filter ):
  print(name)

# Output
"Wessam"
"Essam"

print('*' * 25 )

# [3]

from functools import reduce
nums = [2, 4, 6, 2]

def getNums(n1, n2) :
  return n1 * n2

reduceNums = reduce(getNums, nums)
print(reduceNums)

#  or

result = reduce(lambda n1, n2: n1 * n2 , nums)
print(result)
# Output
96
  
print('*' * 25 )
  

# [4]
skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

for rate , skill in enumerate(reversed(skills), 50) :
  
  if type(skill) != int :
    print(f'{rate} - {skill}')


# Output
"50 - JavaScript"
"52 - Python"
"53 - PHP"
"55 - CSS"
"56 - HTML"

