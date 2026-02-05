# -- Decorators => Intro --

# [1] Sometimes Called Meta Programming
# [2] Everything in Python is Object Even Functions
# [3] Decorator Take A Function and Add Some Functionality and Return It
# [4] Decorator Wrap Other Function and Enhance Their Behaviour
# [5] Decorator is Higher Order Function (Function Accept Function As Parameter)

# [1]
def decorator(func) :
  
 def nasredFunc() :
   
    print('Before')
    
    func()
    
    print('After')
    
 return nasredFunc
    
@decorator    # correct way
def sayHello() :
  print('Hello From SayHello Function')
  
sayHello()
  
# finallDecorator = decorator(sayHello)  # stupied way 
# finallDecorator()

print('*' * 25)
# [2]

def main(function) :
  def nasted() :
    
    print('- before run nasted code or nasted function')
    
    function()
    
    print('- after run nasted code or nasted function')
    
  return nasted

@main
def theSecoundTask() :
  print('Hi, Iam The Secound Task Or Mission ')  



theSecoundTask()



