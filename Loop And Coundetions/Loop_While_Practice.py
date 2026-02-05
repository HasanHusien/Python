# -- Loop => While Training --
# while condition_is_true
#  Code Will Run Until Condition Become False

myFrinds = ["Hassan", "Ahmed", "Gamal", "Ali", "Rayan", "Sara", "Taha"]

a = 0

while a < len(myFrinds):  # a < 10

  # print(f"-{a + 1} {myFrinds[a]}")
  print(f"-{str(a + 1).zfill(2)} {myFrinds[a]}")

  a += 1  

else:

  print("All Friends Printed To Screen.")
