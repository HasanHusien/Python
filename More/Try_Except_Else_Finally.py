# -- Try | Except | Else | Finally --
# Try     => Test The Code For Errors
# Except  => Handle The Errors
# Else    => If No Errors
# Finally => Run The Code


try :
  id = int(input('What is Your Id ? '))
  print('Valid: ', id)
  
except :
  print('Its Not Valid')
  
# [2]

# input always return str soo!
try  : 
  name = (input('What is Your First Name ? '))
  
  print('Valid: ', name)      
  
except :
  print('Its Not Correct Datatype!')

finally : 
  print('The Jop Is Done.')


