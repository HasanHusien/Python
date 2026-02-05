[1]

try :
  
  userNumber =  int(input('whats your number ? '))
  
  if userNumber == 0 :
    print('the number must be larger then 0')
    
  elif len(str(userNumber)) > 1 :
    print('allowed only one Number')  
    
  else :
    print(f'hello, your number is {userNumber}')
  
except :
  
  print('only numbers allowed')

[2]

try :
  letter = input("Add Letter From A to Z ").capitalize()
  
  if len(letter) > 1 :
    
    print('alloed only one char')
    
  elif  letter.isalpha() == False :
    print("The Letter Not In A - Z")
    
  else :
    print(f"you roght {letter}")  


except :
  print('Error Happend ! ')
  
  
[3]
  
def calculate(num1, num2) -> int:
  return num1 + num2 

print(calculate(20, 30)) 


