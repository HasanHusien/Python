my_list = ["H", "S", "A", 1, 2, 3]
my_tuple = ("A", "S", "N")
my_data = []

final_string = ''

for data in zip(my_list, my_tuple):
  # Write Your Code Here
  for char in data :
    
    my_data.append(char)
    
    final_string = ''.join(my_data).capitalize()
    
# print(my_data)
print(final_string) # Hassan


# [2]

my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
my_data = []

final_string = ''

for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
  my_data.append(item1)
  
  final_string = ''.join(my_data[:-2]).capitalize()
  

print(final_string)