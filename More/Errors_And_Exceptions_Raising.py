# [1] Exceptions Is A Runtime Error Reporting Mechanism
# [2] Exception Gives You The Message To Understand The Problem
# [3] Traceback Gives You The Line To Look For The Code in This Line
# [4] Exceptions Have Types (SyntaxError, IndexError, KeyError, Etc...)
# [5] Exceptions List https://docs.python.org/3/library/exceptions.html
# [6] raise Keyword Used To Raise Your Own Exceptions


# raise Exception


num = 1

if num < 0 :
  
  raise Exception('Not Valid Number!')


print('Valid.') 



name = 3

if type(name) != str :
  
  raise ValueError('Value Error!')


print('Valid.')
  
   
   
   