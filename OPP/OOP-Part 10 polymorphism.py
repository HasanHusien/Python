class one:
    
    def funcOne(self):
        print('from class one')
        
        raise NotImplementedError('class must be imblemnted this method required')

class two(one):
    
    def funcOne(self):
        print('from class two')  
        
class three(one):
    
    def funcOne(self):
        print('from class three')
        
        
        
inhertance = two()
inhertance.funcOne()
                