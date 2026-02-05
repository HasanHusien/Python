class member :
    
    def __init__(self, name) :
        
        self.__name = name
        
    def getName(self):
        return self.__name  
    
    def setName(self, newName) :
         self.__name = newName 
        
        
memberOne = member('ahmed')
print(memberOne.getName())
memberOne.setName('Sara')
print(memberOne.getName())
