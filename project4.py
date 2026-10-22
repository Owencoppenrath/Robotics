final = 150
ALIVE = 100
hunger = 100
import time
water = 100
money = 25
day = 1
print("After the events of last week, the police concluded that an unknown intruder entered.")
time.sleep(2)
print("They know not who, not when, and worst of all...")
time.sleep(4)
print("Not why.")
time.sleep(1)
print("")
time.sleep(1)
print(">>>TESTING CONNECTION", end="", flush = True)
time.sleep(1)
print(".", end="", flush = True)
time.sleep(1)
print(".", end="", flush = True)
time.sleep(1)
print(".")
time.sleep(1)
print(">>>CONNECTION ESTABLISHED.")
time.sleep(3)
print("YOU ARE NOW CONNECTED WITH PROJECT 18-5-4-_-19-21-14'S OVERSEER.")
time.sleep(2)
print("")
time.sleep(1)
print(">>> You have exceeded my expectations.")
time.sleep(2)
print(">>> You evaded and almost managed to 'catch' one of my favorite operatives.")
time.sleep(3)
print(">>> Luckily, the police work for us.")
time.sleep(4)
print(">>> I'm suprised you didn't remember that from when you were worming your way through our files.")
time.sleep(4)
print(">>> You want to stop us, if i'm not wrong.")
time.sleep(3)
print(">>> Come find me.")
time.sleep(5)
print("CONNECTION TERMINATED")
time.sleep(3)
print("")
time.sleep(3)
print(">>> GPS LOCATION DOWNLOADED TO DEVICE.")
time.sleep(3)
print("Procceed.")
import time
import random #Hey Josh, a lot of this code is reused from one of my other projects so thats why a  lot of these variables dont line up with the theme;
for i in range (999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):#Hey Josh! You just lost the game!
    if day >= 1:# final:
        print("You have arrived at the DEFIANCE Central Operations Center.")
        time.sleep(2)
        print("You must enter the code.")
        code1 = random.randint(1,35)
        code2 = random.randint(1,35)
        code = int(code2 / code1 + 7 * 7)
        time.sleep(2)
        print(code)
        if int(input(f"Above the keypad is the equation {code2} / {code1} +7 *7 ")) == int(code):
            print("You enter the code...")
            time.sleep(1)
            print("It worked. You enter the facility...")
            time.sleep(2)
            print("To be Continued.")
            quit()
        else:
            print("CODE NOT RECONGNIZED.")
            time.sleep(1)
            print("FACILITY ON LOCKDOWN.")
            time.sleep(3)
            print("And so, you ran...")
            quit()
    if hunger <= 0:
            ALIVE = ALIVE + hunger
    if water <= 0:
                ALIVE = ALIVE + water
    if ALIVE <= 90 :
        ALIVE = ALIVE + random.randint(0,10)
    print(f"Distance Traveled: {day}") 
    print(f"Hydration: {water}, Appetite: {hunger}, Status: {ALIVE}, Balence: {money}")
    camp = random.randint(1,7)
    if camp == 1:
        if input("As you walk down the path, it begins to get steeper...  Y/N ") == "Y":
            print
    elif camp ==2:
        if input("? Y/N ") == "Y":
            print("")
    elif camp == 3:
        print
    elif camp == 4: 
        if input(" Y/N ") == "Y":
            print
    elif camp == 5 :
        print()
    elif camp == 6:
        print
    else:
        print("The path stretches on...")
    hunger = hunger - random.randint (1, 7)
    water = water - random.randint (1, 7)
    day = day + 1
    time.sleep(1)
    print("You continue down the path...")
    time.sleep(2)
    print("")