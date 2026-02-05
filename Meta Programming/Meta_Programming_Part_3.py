
def main(func) :
  
  def nastedWork(n1, n2) :

    if n1 <= 0 or n2 <= 0 :
      
      print('Thire Is A Number Less Then One Check Out!')  # check from main 
      
    func(n1, n2)         # do mission with nasted
    
            
  return nastedWork 


def main2(func) :
  def nasted(n1, n2) :
    
    print('Hello World, Befor Start do Nasted Mission')
    
    func(n1, n2)
    
    print('Hello World, After Finish Nasted Mission')
    
  return nasted  
    


# @main2
@main
def theMission(n1, n2) :
  
  print(n1 + n2) 
  
  
theMission(-11, 12)   



