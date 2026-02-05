# all of these inheritance from other 
class base:
    
    def __init__(self, name):
        
        self.name = name
        
    def getName(name):
        
        print(f'hello dev {name} in your world')
    
        
class branch(base):

    pass
    

class branchTwo(branch):

    pass


branchTwo.getName('hassan')