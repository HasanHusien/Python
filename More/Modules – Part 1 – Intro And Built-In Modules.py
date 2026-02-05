# ---------------------------------
# -- Modules => Built In Modules --
# ---------------------------------
# [1] Module is A File Contain A Set Of Functions
# [2] You Can Import Module in Your App To Help You
# [3] You Can Import Multiple Modules
# [4] You Can Create Your Own Modules
# [5] Modules Saves Your Time
# --------------------------------------------------

# Import Main Module
import random

print('Random:', random.random())


# Show All Functions Inside Module Use dir

# print(dir(random))

# Import One Or Two Functions From Module
from random import randint, random

print('Random Int:',randint(100, 200))
print('The Random Number Is:', random())