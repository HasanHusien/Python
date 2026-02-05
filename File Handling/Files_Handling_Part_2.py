# --------------------------------
# -- File Handling => Read File --
# --------------------------------

myFile = open(r"C:\Users\almostkbal\Desktop\Python\hassan.txt")
print(myFile)


print(myFile)  # File Data Object
print(myFile.name)
print(myFile.mode)
print(myFile.encoding)

# print(myFile.read())

print(myFile.readline(4))
# print(myFile.readline())
print(myFile.readline())

print(myFile.readlines())
# print(myFile.readlines(50))
print(type(myFile.readlines()))

for line in myFile:

  print(line)

  if line.startswith("07"):

    break

# Close The File

myFile.close()