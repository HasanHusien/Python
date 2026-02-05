# Practical Email Slice

firstName = input('What is your First Name ?')
lastName = input('What is your Last Name ?')
email = input('What is your email ?')

midpoint = email.index('@')

print(f'hello {firstName} {lastName}'.capitalize())
print(f'your UserName is {email[:midpoint]} \nyour domin is {email[midpoint + 1:]}'.capitalize())


