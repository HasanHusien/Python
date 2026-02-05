# -----------------------
# -- Boolean Operators --
# -----------------------
# and
# or
# not
# -----------------------

age = 21
country = "Egypt"
rank = 10

allAreRequired = age > 16 and country == "Egypt" and rank > 0
allAreRequired2 = age > 16 and country == "KSA" and rank > 0

print(allAreRequired)  # True
print(allAreRequired2)  # False

oneIsRequired = age > 40 or country == "KSA" or rank > 20
oneIsRequired2 = age > 40 or country == "Egypt" or rank > 20

print(oneIsRequired)  # False
print(oneIsRequired2)  # True

notRequired = not age > 16

print(age > 16)  # True
print(notRequired)  # Not True = False