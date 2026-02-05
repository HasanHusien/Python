# Create Yuor Own Module
 
import sys  #import System

sys.path.append('D//App')  # set On My Pathes
print(sys.path)  

# import from my Module

import My_Module   # get all module
import My_Module as functions # alias name

from My_Module import sayHello # for import spacifice function

My_Module.sayHello('Hassan')
My_Module.getAge(21)