# -- Function Recursion --
# -- To Understand Recursion, You Need to First Understand Recursion --
# 

# Test Word  WWWoooorrrldd  # print(x[1:])

theWord = 'WWWoooorrrldd'

def cleanWord(word) :
  
  if len(word) == 1 :
    
    return word  # bast case 
  
  if word[0] == word[1]:
    
    #if it True Recursion function without word[0]
    return cleanWord(word[1:])
  
  else :
    # if not word[0] == word[1] save word[0] and do function agine 
    return word[0] + cleanWord(word[1:])  



print(cleanWord(theWord))


 