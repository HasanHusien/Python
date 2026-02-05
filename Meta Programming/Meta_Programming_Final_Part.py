def main(func) :
  def nastedMission(*numbers) :
    
    for n in numbers :
      
      if n <= 0 :
        
        print('Thire Is A Number Less Then One, Please Check Out!')
        
    func(*numbers)
    
    
  return nastedMission  
    
    
@main
def mission(n1, n2, n3, n4) :
  
  print(n1 + n2 + n3 + n4)
  
mission(30, 10 , 0, 9) 


# test time

from time import time 

def testMissionTime(func) :  
  
  def nasted():
    
    start = time()
    
    func()
  
    end = time()
    
    print(f'This Takes {end - start} Secounds!')
  
  return nasted    

@testMissionTime
def theJop() :
  
  for n in range(1,150000) :  # perfect Pc 😎
    
    print(n)
  
theJop()  


