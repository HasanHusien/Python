# password challenge

rightPassored = 'hassan@main' 
password = input('Whats Your Password ? ')
tries = 4


# if tries > 0 :
  
while password != rightPassored :
      
  tries -= 1
  
  print (f'wrong password, you still have {'last chance' if tries == 1 else tries} try')
  
  if tries == 0 :
    
    print('maybe should try agine later')
    break
  
  password = input('Whats Your Password ? ')
    
else :
    print('Success !')
    
      


  


