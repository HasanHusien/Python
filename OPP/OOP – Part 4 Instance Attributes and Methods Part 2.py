# -- Object Oriented Programming => Instance Attributes and Methods --
# Self: Point To Instance Created From Class
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself


class employess :
    
    def __init__(self, fName, lName, gender):
        
        self.fName = fName
        self.lName = lName
        self.gender = gender
        
    def getFullName(self) :  # Any Name
        
        if self.gender == 'Male' :
        
            return f"Hello Mr {self.fName} {self.lName}"
        
        elif  self.gender == 'Female' :
            
            return f'Hello Ms {self.fName} {self.lName}'\
                
        else :
            return f'Hello {self.fName} {self.lName}'

    
employessOne = employess('Hassan','Hussien','Male')
employessTwo = employess('Sara','Ahmed','Female')

print(employessOne.getFullName())
print(employessTwo.getFullName())


