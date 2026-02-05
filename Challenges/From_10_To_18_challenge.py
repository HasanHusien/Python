# [1]
name = 'hasan'
age = 22
Country = 'Egypt'
# "Hello 'Osama', How You Doing \ """ Your Age Is "38"" + And Your Country Is: Egypt
print(f'Hello {name}, How You Doing \\ Your Age Is {age} + And Your Country Is: {Country}')

# [2]
print(f'Hello {name}, How You Doing \\ \n Your Age Is {age} \n + And Your Country Is: {Country}')


# [3]
user = 'hassan'

print(f'Second Letter {user[1:2]} \n Third Letter Is {user[2:3]} \n Last Letter Is {user[-1]}')

# Needed Output
# Second Letter Is "a"
# Third Letter Is "s"
# Last Letter Is "n"


# [4]
person = 'Elzero'
print(f'''{person[1:2] + person[2:3] + person[3:4]}\n{person[0] + person[2:3] + person[4:5]}\n{person[4:5] + person[2:3] + person[0]}''')

# Needed Output
# "lze"
# "Ezr"
# "rzE"

# [5]
me = "#@#@hassan#@#@"
print(me.strip('#@',))

# Needed Output
# hassan

#[6]
num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"

print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))

# Needed Output
# 0009
# 0015
# 0130
# 0950
# 1500

#[7]
name_one = "Osama"
name_two = "Osama_Elzero"

print(name_one.center(30,'@',).rstrip('@'))
print(name_two.center(30,'@',).rstrip('@'))


# Needed Output
# @@@@@@@@@@@@@@@Osama
# @@@@@@@@Osama_Elzero

#[8]
nameOne = "OSamA"
nameTwo = "osaMA"
print(nameOne.swapcase())
print(nameTwo.swapcase())

# Needed Output
# osAMa
# OSAma

#[9]
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count('Love'))

# Needed Output
# 2

#[10]

name = "Elzero"
print(name.index('z'))

# Needed Output
# 2


#[11]
msg2 = "I <3 Python And Although <3 hassan hussen"

print(msg2.replace('<3','Love',1))

# Needed Output
# I Love Python And Although <3 Elzero Web School

#[12]
# Needed Output
# I Love Python And Although Love Elzero Web School
print(msg2.replace('<3','Love',))


# [13]
name = "hassan"
age = 22
country = "Egypt"

print(f'My Name Is {name} And My Age Is {age}, And My Country Is {country}')

# Needed Output Using f""
# My Name Is hassan, And My Age Is 22, And My Country Is Egypt

