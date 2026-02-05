# [1]
1+2j

print(1+2j.imag)
print(1+2j.real)

# Print Imaginary Part Here
# Print Real Part Here

# [2]
num = 10
print('{:.10f}'.format(num))
# Needed Ouput
# 10.0000000000

# [3]
number = 159.650

print(int(number))
print(type(int(number)))

# Needed Output
# 159
# <class 'int'>



#[4]
print(100 - 115)
print(50 * 30 )
print(21 % 4 )
print(110 // 11)
print(97 // 20 )

# 100 ? 115 = -15
# 50 ? 30 = 1500
# 21 ? 4 = 1
# 110 ? 11 = 10
# 97 ? 20 = 4

#[5]
friends = ["hassan", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Needed Output
# "hassan" => Method One
# "hassan" => Method Two
# "Mahmoud" => Method One
# "Mahmoud" => Method Two

print(friends[0])
print(friends[0:1])

print(friends[-1])
print(friends[-1:])

#[6]
friendsTwo = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(f'{friendsTwo[0]} {friendsTwo[-3] } {friendsTwo[-1]}')
print(f'{friendsTwo[1]} {friendsTwo[-2]}')

# Needed Output
# "Osama", "Sayed", "Mahmoud"
# "Ahmed", "Ali"

#[7]
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends[-1] = 'hassan'
friends[-2] = 'hassan'
print(friends)

# Needed Output
# ["Osama", "Ahmed", "Sayed", "hassan", "hassan"]

# [8]
friends = ["Osama", "Ahmed", "Sayed"]
friends.insert(0,'abrahim')
friends.append('ali')
print(friends)

# Needed Output
# ["Nasser", "Osama", "Ahmed", "Sayed"]
# ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

#[8]
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

friends.remove('Nasser')
friends.remove('Osama')
print(friends)

friends.remove(friends[-1])
print(friends)
# Needed Output
# ["Ahmed", "Sayed", "Salem"]
# ["Ahmed", "Sayed"]

#[9]
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

print(friends + employees + school)

# Needed Output
# ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

#[10]
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(sorted(friends))
print(sorted(friends,reverse=True))

# print(friends.sort(reverse=True))


# Needed Output
# ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']
# ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']

#[11]
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(friends))

# Needed Output
# 6

#[12]
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[4][0])
print(technologies[4][-1])
# Needed Output
# Django
# Web

#[13]
n = 'hasaan',
print(n)
print(type(n))

# Needed Output

# "Osama"
# <class 'tuple'>

# [14]

popular = ("hassan", "Ahmed", "Sayed")

print(popular)
print(len(popular))

a= list(popular)
a[0] = 'hussien'

b = tuple(a)
print(b)

# Needed Output

# ("Elzero", "Ahmed", "Sayed")
# <class 'tuple'>
# 3 Elements


# [15]

nums = (1, 2, 3)
letters = ("A", "B", "C")

a = nums + letters

print(a)
print(len(a))


# Needed Output

# nums_and_letters_one = (1, 2, 3, "A", "B", "C")
# 6 Elements

# [16]

my_tuple = (1, 2, 3, 4)

a , b, _, c = my_tuple
print(a)
print(b)
print(c)


# Needed Output

# 1
# 2
# 4