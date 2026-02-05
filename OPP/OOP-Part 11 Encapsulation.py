# Encapsulations [public] [protected] [private] 

# public
class member :
    
    def __init__(self, name) :
        self.name = name
        
        
memberOne = member('ahmed')
memberOne.name = 'tarek'
print(memberOne.name)           

#protected 
class typeTwo:
    
    def __init__(self, name):
        self._name = name
        
        
type_2 = typeTwo('hassan')
type_2._name = 'ali'
print(type_2._name)


#private 
class lastType :
    
    def __init__(self, name):
        self.__name = name
        
    def getName(self):
            return f'from inner function {self.__name}'
        
last = lastType('sara')
print(last.getName())  # get name from inner method becouse it only private
# print(last._lastType__name)  this way can het the name
# # print(last.__name)   get error
