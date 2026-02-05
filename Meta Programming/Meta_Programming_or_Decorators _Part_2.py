def main(func1, func2) :
  
  def nasted() :
    print('1- first Mission if you need')
    
    func1()
    
    print('3- The New Mission if You Need')
    
    func2()
    
  return nasted

# @main  if it was on prameter

def hello() :  #func1
  print('2- Hello World, iam a function')
  
def finall() :  #func2
  print('4- Finall Mission, iam a function')  
  
  
allMission = main(hello, finall)

allMission()    


print('*' * 30)


# [2]

def main(func1, func2) :
  
  def nasted() :
    print('1- first Mission if you need')
    
    func1(func2)
    
    print('4- The New Mission if You Need')
    
  return nasted

# @main
def hello(newFunc) :  #func1
  print('2- Hello World, iam a function')
  newFunc()
  
def finall() :  #func2
  print('3- Finall Mission, iam a function')  
  
  
allMission = main(hello, finall)

allMission() 