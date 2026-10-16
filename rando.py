import random
import time
randomnumber = random.randint (1, 10)
health = 100
water = 100
hunger = 100
day = 1
while health >= 1 :
    if hunger <= 0:
        health = health + hunger
    if water <= 0:
            health = health + water
    print(f"Day {day}")
    print(f"Water: {water}, Hunger: {hunger}, Health: {health}")
    place = input("Do you want to go to the Well or the Farm?")
    if place == "well":
         print("you Have A drink")
         water = water + random.randint (1, 20)
    elif place == "farm" :
         print("You eat some food")
         hunger = hunger + random.randint (1, 20)
    else:
        print("You do nothing")     
    hunger = hunger - random.randint (1, 15)
    water = water - random.randint (1, 15)
    day = day + 1
    time.sleep(1)
    