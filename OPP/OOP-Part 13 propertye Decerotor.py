# simply make the methods as properties

class member :
    
    def __init__(self, name, age) :
        
        self.name = name
        self.age = age
        
    @property
    def getName(self):
        return f'hello, {self.name}'
      
    @property
    def getDays(self,) :
         return f'{self.age} Days' 
     
     
emploeyOne = member('hassan',22)

print(emploeyOne.name)
print(emploeyOne.age)
# print(emploeyOne.getName())     
# print(emploeyOne.getDays())  
print(emploeyOne.getName)   #run as property        
print(emploeyOne.getDays)   #run as property
   
     
