fileName = None
verifyCount = 5

while verifyCount != 0 :
  
  try :
  
    print('Please Wright The File Name ')
    print(r'Like This: c:\Users\almostkbal\Desktop\Python')
    
    userFill = input('File Name ? ').strip()
    
    fileName = open(userFill, 'r')
    
    print(fileName.read())
    
    break
  
  except :
    verifyCount -= 1
    
    print('The File Is Not Found')
    print(f'You Still Have {verifyCount} Tries')
    
  # finally :  we dont need this now its not usefull  
  #   print('The Jope Is Done')  

print('The Verifing Is Over.')
  
    


  
  