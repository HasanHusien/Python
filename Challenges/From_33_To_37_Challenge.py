# [1]
print(bool('str'))
print(bool(100))
print(bool(100.100))
print(bool(['str','number','dict','tuple']))

print(bool())
print(bool(''))
print(bool(None))
print(bool([]))

# Needed Output
# True
# True
# True
# True
# False
# False
# False
# False

# [2]
html = 80
css = 60
javascript = 70

midpoint = 50
allRequired = (html > midpoint and css > midpoint and javascript > midpoint)

print(allRequired)

# Needed Output

# [3]
num_one = 10
num_two = 20
num = 20

check_If_One_IsRight = (num > num_one or num > num_two)
check_If_Biggest_Then = (num > num_one and num > num_two)

print(check_If_One_IsRight)
print(check_If_Biggest_Then)

# Needed Output
# True
# False

# [4]
num_one = 10
num_two = 20

allNum = num_one + num_two
exponent = allNum ** 3
stillExponent = exponent % 26000

print(allNum)
print(exponent)
print(stillExponent / 5)
print(type(str(stillExponent / 5)))

# Needed Output

# 30
# 27000
# 1000
# 200.0
# <class 'str'>

