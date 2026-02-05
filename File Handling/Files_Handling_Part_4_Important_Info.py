# -------------------------------------
# -- File Handling => Important Info --
# -------------------------------------

import os

myFile = open(r"C:\Users\almostkbal\Desktop\Python\hassan.txt", "a")
myFile.truncate(5)

myFile = open(r"C:\Users\almostkbal\Desktop\Python\hassan.txt", "a")
print(myFile.tell())

myFile = open(r"C:\Users\almostkbal\Desktop\Python\hassan.txt", "a")
myFile.seek(11)
print(myFile.read())

# os.remove("D:\Python\Files\osama.txt")
