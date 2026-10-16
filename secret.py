import math
solve = 0
while solve == 0:
    step1 = math.sin (int(input("Password?")))
    step2 = math.sqrt(step1)
    if step2 == 0.841907360139213:
        print("You did it!")   
        solve = 1 
    else :
        print("You failed...")