final = 50
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
for i in range (999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):#Hey Josh! You just lost the game! Also this is tha start of the big loop.
    if day >= final: #Hey josh this  is the end of the loop for victory!
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
    print(f"Hydration: {water}, Appetite: {hunger}, Status: {ALIVE}")
    camp = random.randint(1,7)
    if camp == 1:
        if input("You are under attack. A man is running towards you.  Try to dodge? Y/N ") == "Y":
            if random.randint(1,2) == 2:
                print("You dodge and he sprinted away")
            else:
                print("You failed to dodge...")
                health = random.randint(1,10)
                ALIVE -= health
                time.sleep(1)
                print(f"And lost {health} status. The man runs.")
        else:
            health = random.randint(1,10)
            ALIVE -= health
            time.sleep(1)
            print(f"You lost {health} status. The man runs.")
    elif camp ==2:
        if input("? Y/N ") == "Y":
            print("")
    elif camp == 3:
        poison = random.randint (1,50)
        print("You come upon a table in the woods. It is covered in food.")
        time.sleep(2)
        print(f"A sign says 'Take {poison}'")
        take = input("How many do you take? Intiger ")
        if take <= poison:
            print(f"You took {take}")
        else:
            print("You took too much...")
    elif camp == 4: 
        if input(" Y/N ") == "Y":
            print
    elif camp == 5 :
        print("SOMEONE IS COMING.")
        time.sleep(3)
        for i in range (random.randint(1,100)):
            print("HIDE ", end="", flush = True)
            time.sleep(0.05)
        print("HIDE")
        if input("HIDE Y/N ") == "Y":
            print("You hid")
            for i in range(3):
                time.sleep(0.5)
                print(".", end="", flush = True)
            if random.randint(1,10) == 10:
                time.sleep(3)
                for i in range(30):
                    print("HE FOUND YOU")
                    time.sleep(0.05)
                time.sleep(2)
                quit()
            else:
                print("HE moves on...")
        else:
            for i in range(30):
                print("HE FOUND YOU")
                time.sleep(0.05)
            time.sleep(2)
            quit()
    elif camp == 6:
        print("You come across a campsite. There are some water bottles and rations.")
        time.sleep(1)
        if input("Pick them up? Y/N ") == "Y":
            print("You picked them up...")
            hydration = random.randint(1,35)
            food = random.randint(1,20)
            time.sleep(1)
            print(f"You gained {hydration} water and {food} hunger.")
    else:
        print("The path stretches on...")
    hunger = hunger - random.randint (1, 7)
    water = water - random.randint (1, 7)
    day = day + 1
    if ALIVE <= 0 :
        print("You have passed beyond this mortal coil.")
        time.sleep(2)
        print("DEFIANCE ENEMY STATUS: TERMINATED.")
        time.sleep(1)
        quit()
    time.sleep(1)
    print("You continue down the path...")
    time.sleep(2)
    print("")