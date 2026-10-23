final = 50
alive = 100
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
            alive = alive + hunger
    if water <= 0:
                alive = alive + water
    if alive <= 90 :
        alive = alive + random.randint(0,10)
    print(f"Distance Traveled: {day}") 
    print(f"Hydration: {water}, Appetite: {hunger}, Status: {alive}")
    camp = random.randint(1,7)
    if camp == 1:
        if input("You are under attack. A man is running towards you.  Try to dodge? Y/N ") == "Y":
            if random.randint(1,2) == 2:
                print("You dodge and he sprinted away")
            else:
                print("You failed to dodge...")
                health = random.randint(1,10)
                alive -= health
                time.sleep(1)
                print(f"And lost {health} status. The man runs.")
        else:
            health = random.randint(1,10)
            alive -= health
            time.sleep(1)
            print(f"You lost {health} status. The man runs.")
    elif camp ==2:
        print("You see a monster...")
        time.sleep(2)
        print("Of sand.")
        time.sleep(2)
        print("He offers to give you the heimlich manuever at the cost of some thirst.")
        if input("Accept? Y/N ") == "Y":
            time.sleep(2)
            print("He gives you the heimlich.")
            hydration = random.randint(1,10)
            health = random.randint(1,50)
            water -= hydration
            alive += health
            time.sleep(2)
            print(f"You lost {hydration} water and gained {health} status.") 
            time.sleep(3)
            print("Submitted by Raptor.")
            time.sleep(2)
        else:
            print("He gurgles and moves on.")
            time.sleep(2)
    elif camp == 3:
        poison = random.randint (1,50)
        print("You come upon a table in the woods. It is covered in food.")
        time.sleep(2)
        print(f"A sign says 'Take {poison}'")
        take = input("How many do you take? Intiger. ")
        if take <= poison:
            print(f"You took {take}")
            time.sleep(2)
            print("You didn't take too much!")
            time.sleep(2)
            print("The food was extra nourishing!")
            time.sleep(1)
            health = 10 
            hydration = 5
            take = take *2
            print(f"You gained {health} status, {hydration} hydration and {take} nourishment.")
            alive +=health
            water += hydration
            hunger += take
        else:
            print("You took too much...")
            health = random.randint(10,60)
            alive -= health
            time.sleep(2)
            print(f"You were poisoned and lost {health} status.")
    elif camp == 4: 
        if input("The path is blocked by a rock. Climb it or look around? 1 or 2: ") == "1":
            print("You start to climb...")
            if alive > 80:
                change = random.randint(1,3)
                if change == 3:
                    time.sleep(1)
                    print("You fell down...")
                    day -= 5
                    health = random.randint (10,30)
                    time.sleep(1)
                    print(f"You lost {health} status.")
                else: 
                    time.sleep(2)
                    print("You climbed up and over.")
            else:
                change = random.randint(1,2)
                if change == 2:
                    time.sleep(1)
                    print("You fell down...")
                    day -= 5
                    health = random.randint (10,30)
                    time.sleep(1)
                    print(f"You lost {health} status.")
                else: 
                    time.sleep(2)
                    print("You climbed up and over.")
        else: 
            print("You went around...")
            time.sleep(4)
            print("It took a while but you found a way around.")
            starvation = random.randint(5,15)
            hydration = random.randint(5,15)
            time.sleep(2)
            print(f"You progressed but lost a {hydration} water and {starvation} hunger.")
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
    hunger = hunger - random.randint (1, 5)
    water = water - random.randint (1, 5)
    day = day + 1
    if alive <= 0 :
        print("You have passed beyond this mortal coil.")
        time.sleep(2)
        print("DEFIANCE ENEMY STATUS: TERMINATED.")
        time.sleep(1)
        quit()
    time.sleep(1)
    print("You continue down the path...")
    time.sleep(2)
    print("")