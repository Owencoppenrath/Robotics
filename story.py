import time
place = input("YOU WAKE UP. WHERE WILL YOU GO TODAY?")
if place == "Lab" :
    print("You go to the abandoned science lab.")
    time.sleep(1)
    choice = input("Do you want to go to the record room or the lab room")
    if choice == "lab" :
        print("You walk in and see a bunch of lab equipment")
    elif choice == "records" :
        print("You read a bunch of classified files.")
elif place == "home" :
    print("You walk home..."), 
    activity = input("do you want to watch a movie or play a video game?")
    if activity == "movie" :
        print("you watch Ice Age.")
    elif activity == "video game" :
        print("you play minecraft.")
    else :
        print ("you stare at a blank wall instead.")
else :
    print ("You have profound thoughts about the universe")