import time
if input("Play the second game in the sieries? Y/N: ") == "Y":
    import project2
#rep = 0 //Unused code for a possible function to print text one letter @ a time.
#word = input("wird")
#while rep < 10:
#    num = word[rep]
#    print(f"{num}", end = "", flush= True)
#    rep += 1
#    time.sleep(1)
import random
found = 0
noise = 0
seen = 0
disturbance = 0
power = 1
alone = 1
search1 = 0
search2 = 0
leniality = input("On a scale of 1 - 10 what should difficulty be? ")
leniality = int(leniality)
houradd = 2 / leniality
print(".", end= "", flush = True)
time.sleep(1)
print(".", end= "", flush = True)
time.sleep(1)
print(".")
time.sleep(2)
print("You are not alone.")
time.sleep(2)
print("")
print("There is someone at your door.")
time.sleep(2)
answer = input("Do you want to answer the door? Y/N: ")
if answer == "Y":
    print("No one is there... ")
    time.sleep(1)
    print("You thought you saw something in your pheripheral vision, but when you turn you don't see anything.")
    noise += 3
    seen += 5
    disturbance += 7 
else :
    print("The knocking continues for several more minutes before you hear the sound of footsteps receeding.")
time.sleep(2)
hour = 0
while hour <= 12:
    time.sleep(2)
    print("")
    print(f"Hour {hour}.")
    event = random.randint(1,5)
    if event == 1:
        attic = input("Something creaks in the attic... Investigate? Y/N: ")
        if attic == "Y":
            print("As you climb the stairs to the attic...")
            time.sleep(1)
            if random.randint(1,2) == 1:
                print("The wooden plank supporting your foot snaps and your foot falls through the floor.")
                noise += 4
                disturbance += 2 + leniality
                time.sleep(2)
                print("You pull it out and continue upstairs.")
            else:
                print("Nothing happens.")
            time.sleep(1)
            print("When you make it up, you realize the door to the attic is locked.")
            time.sleep(1)
            print("From ", end="", flush= True)
            time.sleep(.4)
            print("i", end="", flush= True)
            time.sleep(.4)
            print("n", end="", flush= True)
            time.sleep(.4)
            print("s", end="", flush= True)
            time.sleep(.4)
            print("i", end="", flush= True)
            time.sleep(.4)
            print("d", end="", flush= True)
            time.sleep(.4)
            print("e...")
    elif event ==2:
        basement =input("You swear you hear footsteps in your basement, investigate? Y/N ")
        if basement == "Y": 
            print("You look in the basement... a fleeting shadow moves.")
            time.sleep(3)
            print("You investigate, and it was just a trick of the light.")
            seen+=7
            noise+=1
            disturbance -= 4
    elif event == 3 and power == 1:
        gener = input("Your power goes out. Go outside to refuel the generator? Y/N: ")
        if gener == "Y":
            print("You walk outside.")
            alone = 0
            time.sleep(1)
            disturbance += 3
            noise += 7
            seen += 2
            print("You refuel the generator.")
            power = 1
        else:
            power = 0
            time.sleep(1)
            print("You decide not to fix the generator.")
            seen -= 2
    elif event == 4:
        tv = input("The TV Turns on. Watch TV or Look for the remote?? 1, 2: ")
        tv = int(tv)
        if tv == 1:
            print("You watch tv...")
            time.sleep(3)
            print("You get bored and decide to look for the remote.")
        remoteplace=random.randint(1,2)
        time.sleep(1)
        searching = input("Look in the couch or on the table? 1, 2: ")
        if searching ==1:
            print("You look in the couch...")
            if remoteplace == 1:
                print("You found it and turned of the TV.")
                disturbance -=3
                seen -= 7
                noise += 3
            else:
                print("It wasn't there. You unplug the TV and continue with your night.")
                distrubance+= 4
                seen+= 3
                noise+= 5
        elif searching ==2:
            print("You look on the table.")
            if remoteplace == 2:
                print("You found it and turned of the TV.")
                disturbance -=3
                seen+=1
                noise += 3
            else:
                print("It wasn't there. You unplug the TV and continue with your night.")
                distrubance+= 4
                seen+= 3
                noise+= 5
    elif event == 5:
        print("Nothing noteworthy happens.")
    else:
        print("You hear breathing behind you in the dark.")
        time.sleep(1)
        print("")
        time.sleep(2)
        print(".", end="", flush=True)
        time.sleep(2)
        print(".", end="", flush=True)
        time.sleep(2)
        print(".")
        time.sleep(2)
        if input("Don't move...") != "":
            alone = 100
            seen = 100 
            disturbanve=100
            noise=100
        time.sleep(1)
        if input("Don't move...") != "":
            alone = 100
            seen = 100 
            disturbanve=100
            noise=100
        time.sleep(1)
        if input("Don't move...") != "":
            alone = 10000
            seen = 10000
            disturbanve=10000
            noise=10000
        time.sleep(7)
    hour += houradd
    found = alone + disturbance + seen + noise 
    if found > 5 + 50 / leniality:
        print("You finally see him.")
        time.sleep(5)
        print("And he sees you.")
        alone = 1
        hide = 1
        print("The time no longer matters.")
        time.sleep(2)
        print("Now, your life is in your hands.")
        time.sleep(1)
        print("Ⱡ₳ĐɎ ₮ł₥Ɇ ₩łⱠⱠ ₦Ø₮ ⱧɆⱠ₱ ɎØɄ ⱧɆⱤɆ")
        police = 0
        arrive = 0
        while hide > 0 and alone >= 1:
            search1 = random.randint(1,4)
            if arrive != 10 and police == 1:
                print("THE POLICE APPROACH")
                arrive += 1
            elif arrive == 10:
                print("THE POLICE ARE HERE.")
                time.sleep(1)
                print("THE MAN LOOKS OUT THE WINDOW...")
                time.sleep(1)
                print("AND TAKES OF RUNNING OUT OF THE BACKDOOR.")
                time.sleep(1) 
                print("TO BE CONTINUED.")
                quit() #The survival ending where the Man flees from the police, you have to call the cops and survive 10 turns.
            print("Hour ???")
            time.sleep(1)
            print("HIDE")
            time.sleep(2)
            search1 = random.randint(1,4)
            place = input("HIDE IN THE KITCHEN, THE BEDROOM, THE ATTIC, OR THE BASEMENT??? 1, 2, 3, 4,")
            place = int(place)
            if place == 1:
                print("YOU RUN INTO THE KITCHEN. YOU LOCK THE DOOR.")
                hideplace=search2
            elif place == 2:
                hideplace = input(" HIDE IN THE WARDROBE, UNDER THE BED, OR CALL THE POLICE? 1, 2, 3,")
                hideplace = int(hideplace)
                search2 = random.randint(1,3)
                if hideplace == 1:
                    print("YOU HID IN THE WARDROBE")
                elif hideplace == 2:
                    print("YOU HID IN THE BED")
                elif hideplace == 3:
                    print("YOU CALLED THE POLICE. THEY WILL ARIVE IN 10 TURNS.")
                    police = 1
                    hideplace=search2
                else:
                    hideplace = search2
                    print("Standing there, you hope and pray H̶̨̨̡̧̛̱͍͕̯̜̗͇̮̣̲̩̬̫̝̬̞̫̼͍̞͚͙̻̤͓͖̮̯͎̘̙͎̦̭̯͇̣̼̣̣̮͚̩͇̙̱͖͎̹̩͍̹͈̭̟̖͓̘͈̺̮̦͔̋̋̈́̀̅́͊̈̀͋̑̏̀̅̆̀̇̇̓̀̿͑̈́͌͛̇͂͋̉͒͒̂͌̋̉͌͒͒͆̅͂̆͋͊̒̓͆̀́͗̊̀͛̉̈́͌̔̾͌̈͒̈́̄̍̚͘͜͝͝ͅĘ̸̨̨̢̡̨̢̨̛̛̛̪̳̻͔͈͔̳͈͍̝̯̦͎̣̘̮̮̣͙̻̝͖̰̫̞̼̻̣͉̓̑̓͑̌͊̏̒͊̇̏͆̐̊̓̾̌̀͛͗̒͛͂̈́̎̑̄̍͌̈́̇̒́͒̀͂͂́͑̉͌̀̾͆̏͆̍̈̏̓͆̓͑̇́͂̈̆̈́̄̅͒́̀͊͛̑̆̓̇̎͒͛̊̈́̒̅̈͌̆̀̕̕̕͘̚͘͝͠͠͝͠͝͝͠͝ Will not appear.")
            elif place ==3:
                print("YOU BARREL UP THE STAIRS...")
                time.sleep(1)
                if random.randint(1,2) == 2:
                    print("BUT YOU TRIPPED...")
                    time.sleep(2)
                    if random.randint(1,2) == 2:
                        print("AND THE MAN FOUND YOU")
                        time.sleep(1)
                        turn = 1
                        while turn != 250:
                            print("H̸̨̧̢̨̡̢̧̨̛̰͓͍̤̱̣̥̱̩̤̬̦̙̬͓̱̖̪̳̻̲̰̹̘̪̗͇̫̟͓̱͉̤̣̙̝͍̫̲̹̝̹̊̏̌͋͊̓͐̆͒̐͒̀̓͛̉̌̅̄͐̔́̽̈͌̉̃̀̔̌͊̏̿͗͌̒̎̀̄̿̈̀̓̌̃̐̔̃̈́̄̉̽̍̓̅͂͊̉͆̊͑̐̋̍̓͊̔̀̔̒̂̿̏̓͂͒̓̾̓̈́̎́̿͛̋̋̿́̈́̐̾̃̐̀͘̚̚̚͜͝͠͝͠͠͝ͅĘ̷̡̢̡̡̢̢̧̢̧̧̡̢̧̨̢̧̨̛͔̳͍̳̬̮͇͕̱̮̣͈̰̣̹͎̤̻̬̤͖̰̞̬͉͕͇̻̠̥̙̬̮͉̣̘̖̪̼̜̹̯͙̯̗͎̣̙̺͖͎̙̰̯͚͓̘̗̼̠͇̯͈͉̫͚͉̪͉̺̺̹̣̙̱̟̘̜̮͔̱̬͇͍̼̩̦̩̫̻̙͓̤̞̰͓̞̲̝͔̪̠̹̱̬̗͎̘͖̜̱̀̂̃́͗̎͑̎́̃̒͒̉́͆̂͋͌͌̃̈́́̇͜͜͝ͅͅ ̸̧̨̡̧̛̛̛̪̰̘̖͚͔̹̯̼͓̝̱̯͇̭̬͖̠͚̰̟̠͇͈͕̼͓̖͈͍̱̝̜̝̪̣͕̘̣͖̠̫̟̈́̆́̓̈̉̂̑̏̀̑̀̔̎͆̓̃͒̑̆̓̑̌͐̒̇͌̾͋͗̐̓̈́̈́̊̃̊̋͋͊̊͐̔̈́͑̾̈́̾̚̚̕͘̕̚̕͜͜͜͝͝͠͝͠͝ͅF̶̢̨̢̛̮͕̜̫̤̘͚̲̥͎̼̬̯͇͈̓̉̾̐̐̍̓̍̽̃̔̿̐̒͊̈́̃̒͗̾͜͜͠͠Ǫ̷̡̧̨̡̢̧̢̛̛̻͓͙̠̣̙͇̜͚͙̘̦̲̲͚͈̫̱͓̘̳̹͖̠͍̻̳̦͇͙̯̮̼̬̟̟͚̼̦̦̹͎̣͚̤̠̭̩̺̼̖͕̠͔͍͎̟̱̬̯̙̠̩̤̒̉̔̊̈́̈́́̉͐̆̏̍̎̽̓̿̈̇̒̿́͂͐̈́̔̿̃̍̃̑̈́͒̀̆̿͗͊̂̊͗̈͋̈̀͆̇̑̈́̔́̓̅̑̀̋̈́̿́̌̆̈́̃̊̋͛̾̌̓̒̿͗̄̓̊́̅̈̅̇́̒̅̈́̀̂̅͋́̊̊͘̚̕͘͘͘͘͜͜͝͝͝͝͝͝ͅƯ̶̡̢̨̧̛̛̛̦̮̗̜̬̮̖̝̙̝̙̞̟̝̖͖͇̩͚̠̫͈̬̥̠̤͍͍͇̤̹̬̪̱͕̳͓͔̦̰̝̞̰͉͍͔͚̪͇̰͙͍͔̺̘̝̦̮͈̲͍̏͐̒́̐̎͐̿͊͒̀́̉͊͋͒̇̊̔̽̍̓̌̌̀̔̑̀̍̐̏́͊͗͗̿̿͆̑̀̽͌̅͆͗̒̒̓̄̑̃̇̒̅̈̔̓̈́͒̓͛͂̑̎̇̓̂̽̀̄̆̃́̏̂̿͌́͆̈̀͌̉͛̿͋̇́͗́̀̈́͂̈́̾̉͋͆̏͌͋̋̈̋͛͂̚̕̚͘̚̚̕̕̚͘͘̕͠͝͝͝͝͝͠͝͝͝͠͝͠͝ͅN̷̨̨̧̡̡̨̧̢̧̡̛͓̭̰͚̟̤̜͕̩̺̭͚͕͔͓̼̳͖͙̰͖̭̲͍͇͓̭̺͎͙͚͈̻̹̗̼̖̝̭͙͓͕̗͉͎̩̻͇͔͓̝̩̞̳̠͇̟̜̫̣͙̫͖͈͎͔̜̰̟̟̗̟̼̣̻͇̲͍̘̞͎͓̼̹̣̣̞̳̻̬̦̭̺̮̤̞͓̬͚̣̝̲̟͕̪̥̍͑̽̔͛̾͑̃̉̈̓̑̇̒̈́̅̑̀͗̑͛̄̄́̾̒͐̍̒̐̈́͒̑͌͛̄̎̀͗͆͑̎͛̊́̋̾̓͛͒́̅̄̈͛̅̆͑̈́͒̅̉̉̓͒͋́̓́͛̄̀̾̿̒͐̋̆͘͘̕̕̕̚͘̚͜͝͝͝͠͝ͅͅͅͅD̸̛̩̊͛̊͒̅̐̀̓̂̉͌̎̋̀͗̅̇̐̎̄̐̈́̀͒͗̈́̀̈̾̑̆̒̂͊́̌͐̈́̄̋̾̄̑̐̋̂͂̒̓̓̏̈́̉͐͌̄̃̊̐͆͒͒̆͛̃̎̇̈́̀̏͋̈́̊̒̇̌̋͊̄̿͂̊͘͘̕̚͝͝͠͝ ̶̛̙̝͓͔̩̥̯̤̙̓̾͑̌̄̎͂̅̓̃̑̂̈́̿̈́͆̍͊̐̑̐̏̏̀̓̆̉͌̉͒̑̏̑͆̊̅̽̎̔͌̌̓̀̽̀̏͛͒́̈́̂̋̏̍̂͐͌̓͊͊́̈́̆͑͆̓̇͊̈́́̽̽̈́̉̑͑̆̈̃̈͊̄̀̔̄́͒͗̓̐͑̋̚̕͘̚̕͘̕̕͝͠͠͝͝͝Y̶̢̢̛͔̬̬̺͙̟̻̹̼͖̰̹͖͎̦̪̤̖̏̀̿̆͗̎̄̿̓̊̂̋͑͆̇͐̿̒̀̊̊̄̎̇̏͛͐̈̍̇̽͘͜͝Ỏ̵͖̮̦̖̳̝͉̞͙̹͎̩̹͉̰̦̗̠͙̹͕̼̐̈́̑͐̆̆̏̉̍͋̍̾̓́̒̉̊͌͐̇̆̐́̀͋̽̀͌̈͂͊́͋͂͋͑̈̋͊͋͗͐́́̈̅̔̿̐͂́́̌̀̀̈́͒̐̀̃̎͊̓̑̀̓̆͊̓͛̾͛̄͂̅̈́́̂͊̀̂̾͆͒̔̓̄͐̇͆̀̃̏̅̀̽̅͘̚̕͘̚̕͠͠͝͝͠͝͝͝Ư̶̡̢̧̨̛̛̛̛̛͓̺̪̻̜̖̣͈̥̗͇̖̗̦͍̬̮͇͖͇̖̣̲̣͇̠̦̪̬̜̭̙̞̐̔̈́̓͆̑̂͛͒̇̍̍̄͑̉͑̐̉́̄͌̋̀̉̄̏́̅͆̈́̇̌́͑̌̔̐͋͗̽̽̈͒̏͋̅̿̊̈̊̊͛̆̋̍͑͑̀̽̈́̀̾͋̓̔̃́̈́͛̓͗͋̒̾̓͑̂͂͋̐̇͊̀͛́̅̂͊̋́̓͊̐͑͗̓̃̃̑̌̓̆͗͗̋̓̃̀́̃̃͛̈́̍͂̚̚͘̕̕̚̚͘͘̚͜͝͝͠͠͝͝͝ͅ")
                            turn += 1
                            time.sleep(.05)
                        print("")
                        time.sleep(1)
                        print("A fatal error has occurred.")
                        time.sleep(1)
                        quit()# Death ending where you tripped and the man found you if the lights are off or the difficulty is hard.
                print("BUT IT WAS STILL LOCKED")
                hideplace = search2
            elif place == 4:
                print("YOU SPRINT DOWN...")
                time.sleep(1)
                if power == 0 or leniality >= 5:
                    if random.randint(1,2) == 2:
                        print("BUT YOU TRIPPED...")
                        time.sleep(2)
                        if random.randint(1,2) == 2:
                            print("AND THE MAN FOUND YOU")
                            time.sleep(1)
                            turn = 1
                            while turn != 250:
                                print("H̸̨̧̢̨̡̢̧̨̛̰͓͍̤̱̣̥̱̩̤̬̦̙̬͓̱̖̪̳̻̲̰̹̘̪̗͇̫̟͓̱͉̤̣̙̝͍̫̲̹̝̹̊̏̌͋͊̓͐̆͒̐͒̀̓͛̉̌̅̄͐̔́̽̈͌̉̃̀̔̌͊̏̿͗͌̒̎̀̄̿̈̀̓̌̃̐̔̃̈́̄̉̽̍̓̅͂͊̉͆̊͑̐̋̍̓͊̔̀̔̒̂̿̏̓͂͒̓̾̓̈́̎́̿͛̋̋̿́̈́̐̾̃̐̀͘̚̚̚͜͝͠͝͠͠͝ͅĘ̷̡̢̡̡̢̢̧̢̧̧̡̢̧̨̢̧̨̛͔̳͍̳̬̮͇͕̱̮̣͈̰̣̹͎̤̻̬̤͖̰̞̬͉͕͇̻̠̥̙̬̮͉̣̘̖̪̼̜̹̯͙̯̗͎̣̙̺͖͎̙̰̯͚͓̘̗̼̠͇̯͈͉̫͚͉̪͉̺̺̹̣̙̱̟̘̜̮͔̱̬͇͍̼̩̦̩̫̻̙͓̤̞̰͓̞̲̝͔̪̠̹̱̬̗͎̘͖̜̱̀̂̃́͗̎͑̎́̃̒͒̉́͆̂͋͌͌̃̈́́̇͜͜͝ͅͅ ̸̧̨̡̧̛̛̛̪̰̘̖͚͔̹̯̼͓̝̱̯͇̭̬͖̠͚̰̟̠͇͈͕̼͓̖͈͍̱̝̜̝̪̣͕̘̣͖̠̫̟̈́̆́̓̈̉̂̑̏̀̑̀̔̎͆̓̃͒̑̆̓̑̌͐̒̇͌̾͋͗̐̓̈́̈́̊̃̊̋͋͊̊͐̔̈́͑̾̈́̾̚̚̕͘̕̚̕͜͜͜͝͝͠͝͠͝ͅF̶̢̨̢̛̮͕̜̫̤̘͚̲̥͎̼̬̯͇͈̓̉̾̐̐̍̓̍̽̃̔̿̐̒͊̈́̃̒͗̾͜͜͠͠Ǫ̷̡̧̨̡̢̧̢̛̛̻͓͙̠̣̙͇̜͚͙̘̦̲̲͚͈̫̱͓̘̳̹͖̠͍̻̳̦͇͙̯̮̼̬̟̟͚̼̦̦̹͎̣͚̤̠̭̩̺̼̖͕̠͔͍͎̟̱̬̯̙̠̩̤̒̉̔̊̈́̈́́̉͐̆̏̍̎̽̓̿̈̇̒̿́͂͐̈́̔̿̃̍̃̑̈́͒̀̆̿͗͊̂̊͗̈͋̈̀͆̇̑̈́̔́̓̅̑̀̋̈́̿́̌̆̈́̃̊̋͛̾̌̓̒̿͗̄̓̊́̅̈̅̇́̒̅̈́̀̂̅͋́̊̊͘̚̕͘͘͘͘͜͜͝͝͝͝͝͝ͅƯ̶̡̢̨̧̛̛̛̦̮̗̜̬̮̖̝̙̝̙̞̟̝̖͖͇̩͚̠̫͈̬̥̠̤͍͍͇̤̹̬̪̱͕̳͓͔̦̰̝̞̰͉͍͔͚̪͇̰͙͍͔̺̘̝̦̮͈̲͍̏͐̒́̐̎͐̿͊͒̀́̉͊͋͒̇̊̔̽̍̓̌̌̀̔̑̀̍̐̏́͊͗͗̿̿͆̑̀̽͌̅͆͗̒̒̓̄̑̃̇̒̅̈̔̓̈́͒̓͛͂̑̎̇̓̂̽̀̄̆̃́̏̂̿͌́͆̈̀͌̉͛̿͋̇́͗́̀̈́͂̈́̾̉͋͆̏͌͋̋̈̋͛͂̚̕̚͘̚̚̕̕̚͘͘̕͠͝͝͝͝͝͠͝͝͝͠͝͠͝ͅN̷̨̨̧̡̡̨̧̢̧̡̛͓̭̰͚̟̤̜͕̩̺̭͚͕͔͓̼̳͖͙̰͖̭̲͍͇͓̭̺͎͙͚͈̻̹̗̼̖̝̭͙͓͕̗͉͎̩̻͇͔͓̝̩̞̳̠͇̟̜̫̣͙̫͖͈͎͔̜̰̟̟̗̟̼̣̻͇̲͍̘̞͎͓̼̹̣̣̞̳̻̬̦̭̺̮̤̞͓̬͚̣̝̲̟͕̪̥̍͑̽̔͛̾͑̃̉̈̓̑̇̒̈́̅̑̀͗̑͛̄̄́̾̒͐̍̒̐̈́͒̑͌͛̄̎̀͗͆͑̎͛̊́̋̾̓͛͒́̅̄̈͛̅̆͑̈́͒̅̉̉̓͒͋́̓́͛̄̀̾̿̒͐̋̆͘͘̕̕̕̚͘̚͜͝͝͝͠͝ͅͅͅͅD̸̛̩̊͛̊͒̅̐̀̓̂̉͌̎̋̀͗̅̇̐̎̄̐̈́̀͒͗̈́̀̈̾̑̆̒̂͊́̌͐̈́̄̋̾̄̑̐̋̂͂̒̓̓̏̈́̉͐͌̄̃̊̐͆͒͒̆͛̃̎̇̈́̀̏͋̈́̊̒̇̌̋͊̄̿͂̊͘͘̕̚͝͝͠͝ ̶̛̙̝͓͔̩̥̯̤̙̓̾͑̌̄̎͂̅̓̃̑̂̈́̿̈́͆̍͊̐̑̐̏̏̀̓̆̉͌̉͒̑̏̑͆̊̅̽̎̔͌̌̓̀̽̀̏͛͒́̈́̂̋̏̍̂͐͌̓͊͊́̈́̆͑͆̓̇͊̈́́̽̽̈́̉̑͑̆̈̃̈͊̄̀̔̄́͒͗̓̐͑̋̚̕͘̚̕͘̕̕͝͠͠͝͝͝Y̶̢̢̛͔̬̬̺͙̟̻̹̼͖̰̹͖͎̦̪̤̖̏̀̿̆͗̎̄̿̓̊̂̋͑͆̇͐̿̒̀̊̊̄̎̇̏͛͐̈̍̇̽͘͜͝Ỏ̵͖̮̦̖̳̝͉̞͙̹͎̩̹͉̰̦̗̠͙̹͕̼̐̈́̑͐̆̆̏̉̍͋̍̾̓́̒̉̊͌͐̇̆̐́̀͋̽̀͌̈͂͊́͋͂͋͑̈̋͊͋͗͐́́̈̅̔̿̐͂́́̌̀̀̈́͒̐̀̃̎͊̓̑̀̓̆͊̓͛̾͛̄͂̅̈́́̂͊̀̂̾͆͒̔̓̄͐̇͆̀̃̏̅̀̽̅͘̚̕͘̚̕͠͠͝͝͠͝͝͝Ư̶̡̢̧̨̛̛̛̛̛͓̺̪̻̜̖̣͈̥̗͇̖̗̦͍̬̮͇͖͇̖̣̲̣͇̠̦̪̬̜̭̙̞̐̔̈́̓͆̑̂͛͒̇̍̍̄͑̉͑̐̉́̄͌̋̀̉̄̏́̅͆̈́̇̌́͑̌̔̐͋͗̽̽̈͒̏͋̅̿̊̈̊̊͛̆̋̍͑͑̀̽̈́̀̾͋̓̔̃́̈́͛̓͗͋̒̾̓͑̂͂͋̐̇͊̀͛́̅̂͊̋́̓͊̐͑͗̓̃̃̑̌̓̆͗͗̋̓̃̀́̃̃͛̈́̍͂̚̚͘̕̕̚̚͘͘̚͜͝͝͠͠͝͝͝ͅ")
                                turn += 1
                                time.sleep(.05)
                            print("")
                            time.sleep(1)
                            print("A fatal error has occurred.")
                            time.sleep(1)
                            quit()# Death ending where you tripped and the man found you if the lights are off or the difficulty is hard.
                time.sleep(1)
                search2 = random.randint(1,3)
                hideplace = input ("HIDE BEHIND A BARREL, IN THE CLOSET OR UNDER THE STAIRS? 1, 2, 3. ")
                if hideplace == 1:
                    print("YOU HIDE BEHIND A BARREL")
                elif hideplace == 2:
                    print("YOU HIDE IN THE CLOSET.")
                elif hideplace ==3:
                    print("YOU HIDE UNDER THE STAIRS.")
                else:
                    print("STANDING THERE, YOU HOPE HE DOES NOT COME DOWN...")
                    hideplace = search2
            else:
                print("COLD SWEAT DRIPS OF YOUR BROW")
                time.sleep(1)
                print("AS THE MAN LUNGES TOWARDS YOU,")
                time.sleep(2)
                print("YOU REALIZE")
                time.sleep(2)
                print("")
                print("Connection Terminated. Target Terminated. Loose End Terminated.")
                quit() #This is one of the bad endings, where if you don't move you don't... win.
            if search1 == place:
                if search2 == hideplace:
                    print("H̶̨̨̡̧̛̱͍͕̯̜̗͇̮̣̲̩̬̫̝̬̞̫̼͍̞͚͙̻̤͓͖̮̯͎̘̙͎̦̭̯͇̣̼̣̣̮͚̩͇̙̱͖͎̹̩͍̹͈̭̟̖͓̘͈̺̮̦͔̋̋̈́̀̅́͊̈̀͋̑̏̀̅̆̀̇̇̓̀̿͑̈́͌͛̇͂͋̉͒͒̂͌̋̉͌͒͒͆̅͂̆͋͊̒̓͆̀́͗̊̀͛̉̈́͌̔̾͌̈͒̈́̄̍̚͘͜͝͝ͅĘ̸̨̨̢̡̨̢̨̛̛̛̪̳̻͔͈͔̳͈͍̝̯̦͎̣̘̮̮̣͙̻̝͖̰̫̞̼̻̣͉̓̑̓͑̌͊̏̒͊̇̏͆̐̊̓̾̌̀͛͗̒͛͂̈́̎̑̄̍͌̈́̇̒́͒̀͂͂́͑̉͌̀̾͆̏͆̍̈̏̓͆̓͑̇́͂̈̆̈́̄̅͒́̀͊͛̑̆̓̇̎͒͛̊̈́̒̅̈͌̆̀̕̕̕͘̚͘͝͠͠͝͠͝͝͠͝ WALKS IN.")
                    time.sleep(1)
                    print("AND HE FOUND YOU")
                    time.sleep(3)
                    turn = 1
                    while turn != 250:
                        print("H̸̨̧̢̨̡̢̧̨̛̰͓͍̤̱̣̥̱̩̤̬̦̙̬͓̱̖̪̳̻̲̰̹̘̪̗͇̫̟͓̱͉̤̣̙̝͍̫̲̹̝̹̊̏̌͋͊̓͐̆͒̐͒̀̓͛̉̌̅̄͐̔́̽̈͌̉̃̀̔̌͊̏̿͗͌̒̎̀̄̿̈̀̓̌̃̐̔̃̈́̄̉̽̍̓̅͂͊̉͆̊͑̐̋̍̓͊̔̀̔̒̂̿̏̓͂͒̓̾̓̈́̎́̿͛̋̋̿́̈́̐̾̃̐̀͘̚̚̚͜͝͠͝͠͠͝ͅĘ̷̡̢̡̡̢̢̧̢̧̧̡̢̧̨̢̧̨̛͔̳͍̳̬̮͇͕̱̮̣͈̰̣̹͎̤̻̬̤͖̰̞̬͉͕͇̻̠̥̙̬̮͉̣̘̖̪̼̜̹̯͙̯̗͎̣̙̺͖͎̙̰̯͚͓̘̗̼̠͇̯͈͉̫͚͉̪͉̺̺̹̣̙̱̟̘̜̮͔̱̬͇͍̼̩̦̩̫̻̙͓̤̞̰͓̞̲̝͔̪̠̹̱̬̗͎̘͖̜̱̀̂̃́͗̎͑̎́̃̒͒̉́͆̂͋͌͌̃̈́́̇͜͜͝ͅͅ ̸̧̨̡̧̛̛̛̪̰̘̖͚͔̹̯̼͓̝̱̯͇̭̬͖̠͚̰̟̠͇͈͕̼͓̖͈͍̱̝̜̝̪̣͕̘̣͖̠̫̟̈́̆́̓̈̉̂̑̏̀̑̀̔̎͆̓̃͒̑̆̓̑̌͐̒̇͌̾͋͗̐̓̈́̈́̊̃̊̋͋͊̊͐̔̈́͑̾̈́̾̚̚̕͘̕̚̕͜͜͜͝͝͠͝͠͝ͅF̶̢̨̢̛̮͕̜̫̤̘͚̲̥͎̼̬̯͇͈̓̉̾̐̐̍̓̍̽̃̔̿̐̒͊̈́̃̒͗̾͜͜͠͠Ǫ̷̡̧̨̡̢̧̢̛̛̻͓͙̠̣̙͇̜͚͙̘̦̲̲͚͈̫̱͓̘̳̹͖̠͍̻̳̦͇͙̯̮̼̬̟̟͚̼̦̦̹͎̣͚̤̠̭̩̺̼̖͕̠͔͍͎̟̱̬̯̙̠̩̤̒̉̔̊̈́̈́́̉͐̆̏̍̎̽̓̿̈̇̒̿́͂͐̈́̔̿̃̍̃̑̈́͒̀̆̿͗͊̂̊͗̈͋̈̀͆̇̑̈́̔́̓̅̑̀̋̈́̿́̌̆̈́̃̊̋͛̾̌̓̒̿͗̄̓̊́̅̈̅̇́̒̅̈́̀̂̅͋́̊̊͘̚̕͘͘͘͘͜͜͝͝͝͝͝͝ͅƯ̶̡̢̨̧̛̛̛̦̮̗̜̬̮̖̝̙̝̙̞̟̝̖͖͇̩͚̠̫͈̬̥̠̤͍͍͇̤̹̬̪̱͕̳͓͔̦̰̝̞̰͉͍͔͚̪͇̰͙͍͔̺̘̝̦̮͈̲͍̏͐̒́̐̎͐̿͊͒̀́̉͊͋͒̇̊̔̽̍̓̌̌̀̔̑̀̍̐̏́͊͗͗̿̿͆̑̀̽͌̅͆͗̒̒̓̄̑̃̇̒̅̈̔̓̈́͒̓͛͂̑̎̇̓̂̽̀̄̆̃́̏̂̿͌́͆̈̀͌̉͛̿͋̇́͗́̀̈́͂̈́̾̉͋͆̏͌͋̋̈̋͛͂̚̕̚͘̚̚̕̕̚͘͘̕͠͝͝͝͝͝͠͝͝͝͠͝͠͝ͅN̷̨̨̧̡̡̨̧̢̧̡̛͓̭̰͚̟̤̜͕̩̺̭͚͕͔͓̼̳͖͙̰͖̭̲͍͇͓̭̺͎͙͚͈̻̹̗̼̖̝̭͙͓͕̗͉͎̩̻͇͔͓̝̩̞̳̠͇̟̜̫̣͙̫͖͈͎͔̜̰̟̟̗̟̼̣̻͇̲͍̘̞͎͓̼̹̣̣̞̳̻̬̦̭̺̮̤̞͓̬͚̣̝̲̟͕̪̥̍͑̽̔͛̾͑̃̉̈̓̑̇̒̈́̅̑̀͗̑͛̄̄́̾̒͐̍̒̐̈́͒̑͌͛̄̎̀͗͆͑̎͛̊́̋̾̓͛͒́̅̄̈͛̅̆͑̈́͒̅̉̉̓͒͋́̓́͛̄̀̾̿̒͐̋̆͘͘̕̕̕̚͘̚͜͝͝͝͠͝ͅͅͅͅD̸̛̩̊͛̊͒̅̐̀̓̂̉͌̎̋̀͗̅̇̐̎̄̐̈́̀͒͗̈́̀̈̾̑̆̒̂͊́̌͐̈́̄̋̾̄̑̐̋̂͂̒̓̓̏̈́̉͐͌̄̃̊̐͆͒͒̆͛̃̎̇̈́̀̏͋̈́̊̒̇̌̋͊̄̿͂̊͘͘̕̚͝͝͠͝ ̶̛̙̝͓͔̩̥̯̤̙̓̾͑̌̄̎͂̅̓̃̑̂̈́̿̈́͆̍͊̐̑̐̏̏̀̓̆̉͌̉͒̑̏̑͆̊̅̽̎̔͌̌̓̀̽̀̏͛͒́̈́̂̋̏̍̂͐͌̓͊͊́̈́̆͑͆̓̇͊̈́́̽̽̈́̉̑͑̆̈̃̈͊̄̀̔̄́͒͗̓̐͑̋̚̕͘̚̕͘̕̕͝͠͠͝͝͝Y̶̢̢̛͔̬̬̺͙̟̻̹̼͖̰̹͖͎̦̪̤̖̏̀̿̆͗̎̄̿̓̊̂̋͑͆̇͐̿̒̀̊̊̄̎̇̏͛͐̈̍̇̽͘͜͝Ỏ̵͖̮̦̖̳̝͉̞͙̹͎̩̹͉̰̦̗̠͙̹͕̼̐̈́̑͐̆̆̏̉̍͋̍̾̓́̒̉̊͌͐̇̆̐́̀͋̽̀͌̈͂͊́͋͂͋͑̈̋͊͋͗͐́́̈̅̔̿̐͂́́̌̀̀̈́͒̐̀̃̎͊̓̑̀̓̆͊̓͛̾͛̄͂̅̈́́̂͊̀̂̾͆͒̔̓̄͐̇͆̀̃̏̅̀̽̅͘̚̕͘̚̕͠͠͝͝͠͝͝͝Ư̶̡̢̧̨̛̛̛̛̛͓̺̪̻̜̖̣͈̥̗͇̖̗̦͍̬̮͇͖͇̖̣̲̣͇̠̦̪̬̜̭̙̞̐̔̈́̓͆̑̂͛͒̇̍̍̄͑̉͑̐̉́̄͌̋̀̉̄̏́̅͆̈́̇̌́͑̌̔̐͋͗̽̽̈͒̏͋̅̿̊̈̊̊͛̆̋̍͑͑̀̽̈́̀̾͋̓̔̃́̈́͛̓͗͋̒̾̓͑̂͂͋̐̇͊̀͛́̅̂͊̋́̓͊̐͑͗̓̃̃̑̌̓̆͗͗̋̓̃̀́̃̃͛̈́̍͂̚̚͘̕̕̚̚͘͘̚͜͝͝͠͠͝͝͝ͅ")
                        turn += 1
                        time.sleep(.05)
                    print("")
                    time.sleep(1)
                    print("A fatal error has occurred.")
                    quit()#Death ending where the man finds you if you hide were he searches.
time.sleep(1)
print("As it turns to dawn, you see a van drive off.")
time.sleep(1)
print("")
print("On the side of the van are the numbers '4-5-6-9-1-14-3-5.'") #This is the good ending, where the DEFIANCE operative leaves after you hide / are not caught by morning.
time.sleep(1)
print("Congratulations ", end="", flush = True)
time.sleep(0.3)
print("you ", end="", flush = True)
time.sleep(0.3)
print("made ", end="", flush = True)
time.sleep(0.3)
print("it ", end="", flush = True)
time.sleep(0.3)
print("to ", end="", flush = True)
time.sleep(0.3)
print("the ", end="", flush = True)
time.sleep(0.3)
print("morning.", end="", flush = True)
time.sleep(.3) 
quit() #The ending if you are not rowdy enough to cause the Man to attack.