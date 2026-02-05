# -- Strings Formatting --
# -- placholder !  
# old way
name = 'hasan'
age = 22
id = 22

print("My Name is: " + name)
# print("My Name is: " + name + " and My Age is: " + age)  # Type Error


# print('hello, my name is: %s \n and my age is: %d' %(name, age))
print('hello, my name is: %s \n and my age is: %d \n and my id is: %d' %(name, age, id))

# %s => String
# %d => Number
# %f => Float


# controling float numbers
num = 11
print('the id is: %f' % num)
print('ican count for %.2f' % num)
print('only four float %.4f' % num)


# controling string 

talk = 'i did alot of an effort on cs world and i really like that !'
print('updat to: %.5s' % talk)



#     New way 



