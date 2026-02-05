# Inputs
num1 = int(input('choose the first number').strip())
num2 = int(input('chhose the secound number').strip())

print(f'Example one 20 + 40 = {num1 + num2}')
print(f'Example two 20 * 40 = {num1 * num2}')
# Needed Output
# Example One 20 + 40 = 60
# Example Two 20 * 40 = 800


# [2]
age = 17

print("App Is Suitable For You" if age > 16 else "App Is Not Suitable For You")
# Needed Output
"App Is Suitable For You" # If Age Larger Than 6
"App Is Not Suitable For You" # if Age Smaller Than 16


# [3]
age =int(input('Whats your age ?'))

months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
secound = minutes * 60

if age > 10 and age < 100 :
  print(f"Your Age In Months Is {months:,} Months")
  print(f"Your Age In weeks Is {weeks:,} weeks")
  print(f"Your Age In days Is {days:,} days")
  print(f"Your Age In hours Is {hours:,} hours")
  print(f"Your Age In minutes Is {minutes:,} minutes")
  print(f"Your Age In secound Is {secound:,} secound")
  
else :
  print('Your age is out of the rang')  
  
# Needed Output
"Your Age In Months Is 456 Months" # Months Example
"Your Age In Weeks Is 1824 Weeks" # Weeks Example


# [4]
# Input Example One "Egypt"
# Input Example Two "Ghana"

country = input("Input Your Country").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

if country in countries :
  print(f'Your Country Eligible For Discount And The Price After Discount Is ${price - discount}')
else :
  print(f"Your Country Not Eligible For Discount And The Price Is ${price}")
  
# Needed Output
"Your Country Eligible For Discount And The Price After Discount Is $70" # Egypt Example
"Your Country Not Eligible For Discount And The Price Is $100" # Ghana Example