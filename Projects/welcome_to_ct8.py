from random import randint


def main():
    playerhaswon = False
    randomNumber = randint(1, 100)
    while (playerhaswon == False):
        print("Please type a number")
        userNumber = int(input())
        if (userNumber == randomNumber):
            print("you win")
            playerhaswon = True
        elif (randomNumber < userNumber):
            print("too high") 
        else:
            print("too low")
main()