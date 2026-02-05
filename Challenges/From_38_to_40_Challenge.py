
# [1]
# Input
name = input('write you name').capitalize()
correctName = name.strip().capitalize()


print(f"Hello {correctName}, Happy To See You Here.")
# Needed Output
# Hello Hassan, Happy To See You Here.


# [2]
# Inputs

validAge = 16
age = int(input('please write your age'))

validCase = age > validAge
invalidCase = age < validAge

if(validCase):
  print(f'Hello Your Age Is {age}, All Articles Is Suitable')
else:
  print(f'Hello Your Age Is Under 16, Some Articles Is Not Suitable For You')

# Needed Output
# "Hello Your Age Is Under 16, Some Articles Is Not Suitable For You" 
# #If Age < 16
# "Hello Your Age Is {Age_Value_If_Larger_Than_16}, All Articles Is Suitable For You" 
# # If Age Is 16+

# [3]
# Inputs
firstName = input('Your first Name ?')
lastName = input('Your last Name ?')

validFirstName = firstName.strip().capitalize()
validLastName = lastName[0].strip().capitalize()

print(f"Hello {validFirstName} {validLastName}.") # Example "Osama M.")

# Needed Output
# "Hello {First_Name} {First_Letter_From_Second_Name}." # Example "Osama M."

# [4]
# Inputs
email = input('please write your email').capitalize()
midpoint = email.index('@')
dot = email.index('.')

name = email[:midpoint].lower()
websiteName = email[midpoint + 1:dot].lower()
domainName = email[dot + 1:].lower()


print(f'Your Name Is {name}')
print(f'Email Service Provider Is {websiteName}')
print(f"Top Level Domain Is {domainName}")

"Hassan@Nn.Sa" # Email
# Needed Output
"Your Name Is Osama"
"Email Service Provider Is nn"
"Top Level Domain Is sa"