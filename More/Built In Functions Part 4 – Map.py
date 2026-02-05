# -- Built In Functions => Map --

# [1] Map Take A Function + Iterator
# [2] Map Called Map Because It Map The Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function

names = ['Hassan','Ali', "Ahmed"]

def textGenrator(text) :
  return f'Hello Dev {text.capitalize().strip()}'

allText = map(textGenrator, names)
print(allText)  # 0x0000018F95B63A40

for item in  list(map(textGenrator, names)):
  print(item)


for name in list(map((lambda n : f"Hello Dev {n.capitalize()}"),names)):
  print(name)