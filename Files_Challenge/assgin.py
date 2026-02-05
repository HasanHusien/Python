import os

print(os.getcwd())

i = 1
while i < 51 :
  
  txt = open(rf'c:\Users\almostkbal\Desktop\File\file{i}.txt','w')
  
  if i == 1 :
    txt.write(f'Hassan Made This, file number: {i}\n')
    txt = open(rf'c:\Users\almostkbal\Desktop\File\file{i}.txt', 'a')
    txt.write(f'Appended => Hassan Made This \n' * 5)
    
  elif i == 25 :
    txt.write('special-text')
    
  elif  i == 10  :
    txt.write('Hassan Passed From Hire ') 
    
    
  else :  
    txt.write(f'File Number: {i}')
    
  i += 1
  
# print(os.getcwd())
print(os.path.abspath(__file__))

txt = open(rf'c:\Users\almostkbal\Desktop\File\file1.txt')

lines = txt.readlines()  
txt.seek(0)                    
content = txt.read()       


print(f'Number Of Lines Is => {len(lines)}')
print(f'Number Of Words Is => {len(content.split())}')
print(f'Number Of Chars Is => {len(content)}')
print(f'Number Of "h" Char Is => {content.count("h")}')

# "Number Of Lines Is => 51"
# "Number Of Words Is => 255"
# "Number Of Chars Is => 1268"
# "Number Of "l" Char Is => 102"