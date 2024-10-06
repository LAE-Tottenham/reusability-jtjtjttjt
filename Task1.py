# Help! My code is too messy :( Please help me organise it and extract out the duplications.

# Define your reusable functions here:
# Make sure each function only does ONE thing!!!!!!!!!!!



###########################################

import math
from T1functions import *



hyp1=firstHyp()
hyp2=secondHyp()
weird_answer = triangle(hyp1,hyp2)
print(weird_answer)

validTask=False
while validTask==False:
    task=int(input("pick the task you want to perform: 1. pythagoras 2. soh 3. cah 4. toa 5. cosine rule 6. sine rule"))
    if task==1: 
        ans=firstHyp()
        validTask=True
    elif task==2:
        ans=soh()
        validTask=True
    elif task==3:
        ans=cah()
        validTask=True
    elif task==4:
        ans=toa()
        validTask=True
    elif task==5:
        ans=cosineRule()
        validTask=True
    elif task==6:
        ans=sineRule()
        validTask=True
    else:
        print("please enter a valid task number")
print(ans)



# After you have written the reusable functions, answer the following:
# Questions:
# 1. What are the preconditions for your code not to break? the lengths and widths must be greater than 0

# 2. Validate the user's input based on your preconditions.

# 3. Why was it useful to use reusable components in this case? Please mention at least 2 reasons and don't forget to contextualise.
#One reason why reusable components are useful is because they can save time as the functions made can be reused in other programs. For example, the functions firstHyp() and secondaryHyp() can both be reused in other programs to find the hypotenuse of any tiangle that the user enters.
#Another reason why reusable components are useful is because it improves the reliability of your programs, as the functions made have already been tested and so can be reusued without needing further testing.

# Further Tasks:
# 1. Put your functions in seperate appropriate files and import them in.
# 2. In your new file add functions for SOH CAH TOA. Also for the sine and cosine rule.
# 3. Let the user choose whether they would like to use Pythogras, SOH, CAH, TOA, sine or cosine rule. Then ask for the relavent information and return the result to them.
# 4. Make sure all of your functions (except the main one) only do ONE thing or process.

# Extension:
# After you calculate the the result for the user. Use a library like Turtle to draw an approximation of their triangle for them.
# Hint: import the functions in drawing_functions.py and call them. See what happens. BTW check out the turtle docs for further info on how to use Turtle. 
