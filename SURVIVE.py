import random
import time
randomnumber = random.randint (1, 10)
health = 100
water = 100
hunger = 100
money = 25
day = 1
final = 50
if input("Custom end date? Y/N ") == "Y":
    final = input("How many days? Intiger. ")
time.sleep(1)
print(f"Last {final} days on the path.")
time.sleep(1)
print("You ready your belonings and set of onto The Path...")
time.sleep(1)
input("ENTER to begin")
while health >= 1:
    if hunger <= 0:
        health = health + hunger
    if water <= 0:
            health = health + water
    if health <= 90 :
        health = health + random.randint(0,10)
    print(f"Day {day}") 
    print(f"Water: {water}, Hunger: {hunger}, Health: {health}, money: {money}")
    camp = random.randint(1,7)
    if camp == 1:
         if input("You arrive at an abandoned camp. There are some waterbottles and rations. Pick them up? Y/N ") == "Y":
              tempwater = random.randint(1,10)
              tempfood = random.randint(1,10)
              hunger = hunger + tempfood
              water = water + tempwater
              print(f"You drank {tempwater} water and ate {tempfood} food!")
    elif camp ==2:
        if input("You come upon a town... trade 10 money for 10 food and 10 water? Y/N ") == "Y":
            if money >= 10 :
                print("You traded 10 money...")
                print("Gained 10 water and 10 food")
                hunger = hunger + 10
                water = water + 10
                money = money - 10
            else :
                print("But you could not afford it...")
    elif camp == 3:
        print("As you walk down the path...")
        time.sleep(2)
        print("You are attacked by a bear.")
        healthtemp = random.randint(5, 45)
        time.sleep(1)
        health = health - healthtemp
        print(f"You managed to fend it off, but lost {healthtemp} health")
    elif camp == 4: 
        if input("You arrive at a town. Tell the stories of your adventures? Y/N ") == "Y":
            story = random.randint(1,4)
            if story == 1:
                print("A girl throws you some coin...")
                moneytemp = random.randint(1,7)
                time.sleep(1)
                print(f"Gained {moneytemp} Money.")
                money = money +moneytemp
            elif story == 2:
                print("No one listens...")
                time.sleep(2)
            elif story == 3:
                print("A man gives you some bread.")
                tempfood = random.randint(5,15)
                hunger = tempfood + hunger
                time.sleep(1)
                print(f"You gained {tempfood} hunger.")
            else :
                if health <= 75 :
                    print("A doctor sees you...")
                    doctor = input("and offers to heal your wounds for 20 Money. Y/N ")
                    if doctor == "Y" and money >= 20 :
                        print("The Doctor heals you.")
                        health = 100
                    elif doctor == "Y" and money < 20 :
                        print("You don't have enough money. The doctor leaves.")
                    else:
                        print("The doctor leaves.")
    elif camp == 5 :
        drink = input("You found a well! Drink from it? Y/N ")
        if drink == "Y":
            print("You drank from the Well!")
            tempwater = 0
            tempwater = 10
            water = tempwater + water
            print(f"You drank {tempwater} Water!")
            if random.randint(1,5) == 5 :
                healthtemp = random.randint(5,25)
                print(f"But you got infected and lost {healthtemp} Health...")
                health = health - healthtemp
        else:
            print("You didn't drink the water.")
    elif camp == 6:
        print("As you walk down the path...")
        time.sleep(1.5)
        print("You are attacked by bandits.")
        time.sleep(1)
        rob = random.randint(5,35)
        bandit = input(f"The Bandit Leader wants {rob} money. Y/N ")
        if bandit == "Y" and money >= rob:
            time.sleep(1)
            print(f"You gave them {rob} Money...")
            robchance = random.randint(1,2)
            time.sleep(1.5)
            if robchance == 1:
                print("But they attacked anyway...")
                healthtemp = random.randint(10,35)
                time.sleep(1)
                print(f"You lost {healthtemp} Health and {rob} Money.")
                health = health - healthtemp
                money = money - rob
            else:
                time.sleep(1)
                print("The bandits leave...")
                time.sleep(1)
                money = money - rob
                print(f"You lost {rob} money...")
        else :
            print("They beat you up and rob you.")
            temphealth = random.randint(3,30)
            if money >= 2:
                rob = random.randint(1,money)
            else: 
                rob = money
            time.sleep(1)
            print(f"You lost {rob} money and {temphealth} health.")
            health = health - temphealth
            money = money - rob
    else:
        print("The path stretches on...")
    hunger = hunger - random.randint (1, 7)
    water = water - random.randint (1, 7)
    day = day + 1
    time.sleep(1)
    print("You continue down the path...")
    time.sleep(2)
    print("")
    if day == final :
        print("")
        time.sleep(1)
        print("And finaly... ")
        time.sleep(2)
        print("You have arrived at your Destination.")
        time.sleep(2)
        print(f"Final stats: Money: {money}, Health: {health}, Hunger: {hunger}, Water: {water}")
        print("")
        time.sleep(4)
        print(f"After {final} days...")
        time.sleep(1)
        print("You have reached the end of The Path.")
        print("Good job!")
        time.sleep(2)
        quit()
if health <= 0:
    time.sleep(3)
    print("But this time you didn't make it off it.")
    time.sleep(1)
    print("")
    print(f"Final stats: Money: {money}, Health: {health}, Hunger: {hunger}, Water: {water}")
    time.sleep(3)
    quit()
