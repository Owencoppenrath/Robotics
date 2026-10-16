import random
word_list = ["heart","loopy","audio","laugh","trial"]
hidden_word = random.choice(word_list)
output = "0"
rep = 0
while output != "🟩🟩🟩🟩🟩" or rep != 6 :
    guess_word = input("What is your guess: ")
    output = ""
    num = 0
    while num <= 4:
        if guess_word[num] == hidden_word[num]:
            output += "🟩"
        elif guess_word[num] in hidden_word:
            output += "🟨"
        else:
            output += "⬛"
        num = num + 1
    rep + 1
    print(output)
    if output == "🟩🟩🟩🟩🟩" :
        print("You Win!")
        quit()