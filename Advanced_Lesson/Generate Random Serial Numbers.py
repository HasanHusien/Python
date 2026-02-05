# import module
import string
# import for get random of any thing
import random

print(string.digits)  #get random Numbers
print(string.ascii_letters)  #get random letters
print(string.ascii_lowercase)  #get random letters lowercase
print(string.ascii_uppercase) #get random letters uppercase

def make_serial(count):

  all_chars = string.ascii_letters + string.digits
  # print(all_chars)

  chars_count = len(all_chars)
  # print(chars_count)

  serial_list = []

  while count > 0:

    random_number = random.randint(0, chars_count - 1)

    random_character = all_chars[random_number]

    serial_list.append(random_character)

    count -= 1  # count = count - 1

  print("".join(serial_list))

make_serial(10) #get the random serial