import random
guessnum = 0
done = 0
hiddennumber = random.randint(-1,999999999999999999999999999999999)
for i in range(int(input("GIVE ME YOUR NUMBERS"))):
    guess = int(input("Pick a number"))
    if guess == hiddennumber:
        print("YOUR A CHEATER")
        quit()
    else: 
        print("ANOTHER ONE BITES THE DUST")
        print("Fun fact -1 is also an answer!")
        if guess > hiddennumber:
            print("Your number is bigger than the hidden number")
        else:
            print("Your number is smaller than the hidden number")
#print(hiddennumber)
print(hiddennumber)