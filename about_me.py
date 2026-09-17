print("My name is Owen Coppenrath")
print("I was born in ST. Luis.")
print("I currently live in Seattle.")
print("I am 13 years old.")
print("I have a dog named Nori.")
name = input("what is your name?")
print(f"Hello {name}!")
if name == " Owen":
    print("Secret message!")
    print("This only happens if you type 'Owen' Into the name input!")
    true = input("Are you actually Owen?")
    if true == " Yes":
        print("Yay!")
    else:
        print("Don't impersonate me!")