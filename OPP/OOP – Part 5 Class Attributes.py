
class employess :
    
    notAllowedNames =['Hell','Damn','Shit']
    
    usersNumbeers = 0
    
    def __init__(self, fName, lName, gender):
        
        self.fName = fName
        self.lName = lName
        self.gender = gender
        employess.usersNumbeers += 1        
        
    def getFullName(self) :  # Any Name
        
        if self.fName in employess.notAllowedNames :
            
            raise ValueError('These Names Are Not Allowed')  # make Error
        
        else :
        
            if self.gender == 'Male' :
            
                return f"Hello Mr {self.fName} {self.lName}"
            
            elif  self.gender == 'Female' :
                
                return f'Hello Ms {self.fName} {self.lName}'\
                    
            else :
                return f'Hello {self.fName} {self.lName}'
            
    def removeEmployees(self) :
        
        employess.usersNumbeers -= 1
        
        return f'Member {self.fName} Deleted'        
    
print(employess.usersNumbeers)

employessOne = employess('Hassan','Hussien','Male')
employessTwo = employess('Sara','Ahmed','Female')
employessThree = employess('Shit','Hell','Female')

print(employess.usersNumbeers)

print(employessThree.removeEmployees())

print(employess.usersNumbeers)

# print(employessOne.getFullName())
# print(employessTwo.getFullName())
# print(employessThree.getFullName())



