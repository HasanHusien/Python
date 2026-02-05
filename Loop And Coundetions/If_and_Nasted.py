# ---------------
# -- Nested If --
# ---------------

userName = "Hassan"
isStudent = True
userCountry = "Egypt"
courseName = "Python Course"
discount = 100

if userCountry == "Egypt" or userCountry == "KSA" :

  if isStudent == True:

    print(f"Hi {userName} Because U R From {userCountry} And Student")
    print(f"The Course \"{courseName}\" Price Is: ${discount - 90}")

  else:

    print(f"Hi {userName} Because U R From {userCountry}")
    print(f"The Course \"{courseName}\" Price Is: ${discount - 80}")


elif userCountry == "Kuwait" or userCountry == "Bahrain":

  print(f"Hi {userName} Because U R From {userCountry}")
  print(f"The Course \"{courseName}\" Price Is: ${discount - 50}")

else:

  print(f"Hi {userName} Because U R From {userCountry}")
  print(f"The Course \"{courseName}\" Price Is: ${discount - 30}")