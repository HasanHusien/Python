# [1]
def reverse_string(my_string):
  # Your Code Here
  yield sorted (my_string, reverse = True)

# Reverse The String
for c in reverse_string('Hassan'):
  print(c)
  
  
  
# [2]
# Create Your Decorator Here
def main(func1, func2) :
  def nasted() :
    
    print("Sugar Added From Decorators")
    
    func1()
    
    print('*' * 20)
    
    print("Sugar Added From Decorators")
    
    func2()
    
    print('*' * 20)
    
  return nasted  
  
def make_tea():
  print("Tea Created")
  
def make_coffe():
  print("Coffe Created")
  
  
runAll = main(make_tea, make_coffe)  

runAll()

# Needed Output

"Sugar Added From Decorators"
"Tea Created"
"####################"
"Sugar Added From Decorators"
"Coffe Created"
"####################" 