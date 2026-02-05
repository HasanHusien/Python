#  [1]
my_list = [1, 2, 3, 3, 4, 5, 1]

Unique = set(my_list)
print(Unique)
a = list(Unique)
print(type(a))
a.pop()
print(a)

# Needed Output
# 1, 2, 3, 4, 5
# <class 'list'>
# 1, 2, 3, 4

print('_' * 25)

# [2]
nums = {1, 2, 3}
letters = {"A", "B", "C"}

print(nums | letters)
print(nums.union(letters))
print(f'{nums | letters}')

# Needed Output
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}
# {1, 2, 3, "A", "B", "C"}

print('_' * 25)

# [3]
my_set = {1, 2, 3}
letters = {"A", "B", "C"}

print(my_set)
my_set.clear()
print(my_set)

letters.discard('C')
my_set.update(sorted(letters))
print(my_set)

# Needed Output
# {1, 2, 3}
# set()
# {"A", "B"}

print('_' * 25)


# [4]
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

print(set_one.issubset(set_two))
# Needed Output
# True

# [5]
# Create Dictionary Here
skills = {
  'HTML': 'Progress Is 90%',
  'CSS' : "Progress Is 80%",
  "Python" : "Progress Is 85%"
}
skills['Ai'] = 'Progress Is 30%'

print("HTML",skills.get('HTML'))
print("CSS",skills.get('CSS'))
print("Python",skills.get('Python'))
print("Ai",skills.get('Ai'))

# Needed Output

# "HTML Progress Is 90%"
# "CSS Progress Is 80%"
# "Python Progress Is 30%"

# "AI Progress Is 20%"