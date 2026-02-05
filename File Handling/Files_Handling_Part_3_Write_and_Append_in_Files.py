#  File Handling => Write and Append In File 

# w => This Prop Remove Lagcy Text And Rghting A New Text
# a => Add Text With The Legacy Text
import os
print(os.getcwd())
myTxt = open(r"C:\Users\almostkbal\Desktop\Python\hassan.txt",'w')

myTxt.write('This Is Your Data:\n')
myTxt.write("""name: Hassan
  age: 21
  skills: ["HTML", "CSS", "JavaScript"]
  isDeveloper": True\n\n"""
)

# myTxt.write('dev.hassan\n' * 10)

list = ['Node.js\n', 'Express.js\n', 'RestApi\n\n']
myTxt.write('I ,ill Learn This Topics At This Year:\n')
myTxt.writelines(list)

myTxtExtra = open(r"C:\Users\almostkbal\Desktop\Python\hassan.txt",'a')

myTxtExtra.write("2025 Remember This !")


