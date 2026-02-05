# -- Object Oriented Programming => Instance Attributes and Methods --
# --------------------------------------------------------------------
# Self: Point To Instance Created From Class
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# -----------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself

class member :
    
    def __init__(self, firstName, middelName ,lastName):
        
        self.fName = firstName
        self.mName = middelName
        self.lName = lastName
        
        
memeberOne = member('Hassan','Hussien',"mohmed")  
memeberTwo = member('Ahmed','Tarek',"Ali")  
memeberThree = member('Sara','Mai',"Jhon")  

print(memeberOne.fName, memeberOne.mName, memeberOne.lName)  
print(memeberTwo.fName, memeberTwo.mName)
print(memeberThree.fName)    
        