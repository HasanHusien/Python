# -- Strings Formatting --
# -- placholder !  
# old way
name = 'hasan'
age = 22
id = 22

print("My Name is: " + name)
# print("My Name is: " + name + " and My Age is: " + age)  # Type Error


# print('hello, my name is: %s \n and my age is: %d' %(name, age))
print('hello, my name is: {:s} , age is: {:d} , id is: {:d}'.format(name, age, id))

# %s => String
# %d => Number
# %f => Float


# controling float numbers
num = 11
print('the id is: {:f}'.format(num))
print('ican count for {:.2f}'.format(num))
print('only four float {:.4f}'.format(num))


# # controling string 

talk = 'i did alot of an effort on cs world and i really like that !'
print('updat to: {}'.format(talk))
print('updat to: {:.5s}'.format(talk))


# Format Money

myMoney = 500162350198

print("My Money in Bank Is: {:d}".format(myMoney))
print("My Money in Bank Is: {:_d}".format(myMoney))
print("My Money in Bank Is: {:,d}".format(myMoney))


# ReArrange Items

a, b, c = "One", "Two", "Three"

print('Welcom, {} {} {}'.format(a,b,c))
print('Welcom, {2} {1} {0}'.format(a,b,c))
print('Welcom, {1} {0} {2}'.format(a,b,c))


x, y, z = 10, 20, 30

print('Hello, {:d} {:d} {:d}'.format(x,y,z))
print('Hello, {} {} {}'.format(x,y,z))
print('Hello, {1} {0} {2}'.format(x,y,z))
print('Hello, {2} {1} {0}'.format(x,y,z))
print('Hello, {2:f} {1:f} {0:f}'.format(x,y,z))
print('Hello, {2:.3f} {1:.3f} {0:.3f}'.format(x,y,z))


# Format in Version 3.6+
# like java script 

dev= 'hasan'
age = 22
id = 32

print(f"hello, Developer {dev} with age {age}") # f is core 
print(f"hello dev {dev}, you are win congraltulations!")






