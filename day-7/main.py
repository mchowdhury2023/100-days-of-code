import random

word_list = ["roney", "kiyan", "tasnia"]

chosen_word = random.choice(word_list)

word = ""
for _ in chosen_word:
    word += "_"

isGameOver = False
countLife = 5

while not isGameOver:
    
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for position in range(len(chosen_word)):
            
            if chosen_word[position] == guess:
                word = word[:position] + guess + word[position + 1:]
        if "_" not in word:
            isGameOver = True
            print(f"congratulations you guessed the word: {word} ")
            break
        print(word)
    else:
        countLife -= 1
        if countLife == 0:
            isGameOver = True
            print(f"You Lost!! The word is : {chosen_word} ")
            break
        print(f"The letter '{guess}' is not in the string.")
        print(f"Guess the remaining blanks of word {word}\n You have {countLife} life remaining")

print("Game Over! ")