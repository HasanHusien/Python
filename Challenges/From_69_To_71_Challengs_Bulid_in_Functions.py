# [1]
values = (0, 1, 2)

if any(values): # its true ,ill run

  my_var = 0

my_list = [True, 1,  1, ["A", "B"], 10.5, my_var] # [True, 1,  1, ["A", "B"], 10.5, 0] 

# [True, 1,  1, ["A", "B"] or  [True, 1,  1, ["A", "B"], 10.5, 0], [True, 1,  1, ["A", "B"], 10.5, 0] 
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

  print("Good")

else:

  print("Bad")
  # its prented good becouse is condtion => all(my_list[:4])
  
  

# [2]
v = 40
my_range = list(range(v)) 
#sum(my_range, v) = 820, pow(v, v, v) = 0
print(sum(my_range, v) + pow(v, v, v))  # 820

# [3]
n = 20

# print(round(190 / 20)) = 10 
# print(round(sum(l) / n)) = 10
l = list(range(n))
if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):

  print("Good")

# Output => Good

# [4] Hardest !

# my_all
def my_all (list) :
  for item in list :
    if not item :
      
      return False
    
  return True
print(my_all([1, 2, 3])) # True
print(my_all([1, 2, 3, []])) # False


# # my_any

def my_any(list) :
  for item in list :
    if item :
      return True
    
  return False  
print(my_any([0, 1, [], False])) # True
print(my_any([(), 0, False])) # False

# # my_min

def my_min(values):
    smallest = values[0]
    for v in values:
        if v < smallest:
            smallest = v
    return smallest
    
  
    
print(my_min([10, 100, -20, -100, 50])) # -100
print(my_min((10, 100, -20, -100, 50))) # -100

# # my_max
def my_max(values):
    Largest = values[0]
    for v in values:
        if v > Largest:
            Largest = v
    return Largest
  
print(my_max([10, 100, -20, -100, 50, 700])) # 700
print(my_max((10, 100, -20, -100, 50, 700))) # 700