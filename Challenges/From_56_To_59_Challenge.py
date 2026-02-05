# [1]

def dealWithNums(num1, num2, type = 'a') :
  
  # additionProcess =  type == 'AdD' or type == 'a' or type == 'A'
  # subtractProcess = type == 'S' or type == 'subTRACT' 
  # multiplyProcess = type == 'Multiply' or type == 'm'
  
  additionProcess  = type in ['add', 'AdD', 'a', 'A']
  subtractProcess  = type in ['s', 'S', 'subtract', 'subTRACT']
  multiplyProcess  = type in ['m', 'M', 'multiply', 'Multiply']
  
  if  additionProcess :
   return num1 + num2
 
  elif subtractProcess : 
    return num1 - num2  
  
  elif multiplyProcess :
    return num1 * num2


# Tests
print(dealWithNums(10, 20)) # 30
print(dealWithNums(10, 20, "AdD")) # 30
print(dealWithNums(10, 20, "a")) # 30
print(dealWithNums(10, 20, "A")) # 30

print(dealWithNums(10, 20, "S")) # -10
print(dealWithNums(10, 20, "subTRACT")) # -10

print(dealWithNums(10, 20, "Multiply")) # 200
print(dealWithNums(10, 20, "m")) # 200


# [2]
# Input
def userData(name ,*skills) :
  
  if skills :
    print(f'hello {name} your skills is :')
    
    for skill in skills :
      
      print(f'- {skill}')
      
  else :
    print(f"Hello {name} You Have No Skills To Show")
        
    
userData("Hassan",'ai aginet','node','next','react')

# Output
"Hello Osama Your Skills Is"
"- HTML"
"- CSS"
"- JS"
"- Python"


# [3]
# Input
def sayHello (name = 'Unknown', age = 'Unknown', country = 'Unknown'):
  
  return f"Hello {name} Your {age} Is 38 And You Live In {country}"

  
  
print(sayHello("hassan", 21, "Egypt"))

# Output
"Hello Osama Your Age Is 38 And You Live In Egypt"

