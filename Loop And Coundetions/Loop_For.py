# Loop => For 
# for item in iterable_object :

myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in myNumbers:

  if number % 2 == 0:  # Even

    print(f"Number: {number} Is Even.")

  else:

    print(f"Number: {number} Is Odd.")

else:

  print("The Loop Is Done")

myName = "hassan"

for letter in myName:

  print(f"{letter.upper()}")