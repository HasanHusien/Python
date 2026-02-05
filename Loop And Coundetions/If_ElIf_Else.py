# --------------------
# --  Control Flow  --
# -- If, Elif, Else --
# -- Make Decisions --
# --------------------

userName = "Hassan"
userCountry = "Egypt"
courseName = "Python Course"
discount = 100

if userCountry == "Egypt":

  print(f"Hello {userName} Because You Are From {userCountry}")
  print(f"The Course \"{courseName}\" Price Is: ${discount - 80}")

elif userCountry == "KSA":

  print(f"Hello {userName} Because You Are From {userCountry}")
  print(f"The Course \"{courseName}\" Price Is: ${discount - 60}")

else:

  print(f"Hello {userName} Because You Are From {userCountry}")
  print(f"The Course \"{courseName}\" Price Is: ${discount - 30}")