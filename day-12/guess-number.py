from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#function to check user's guess and actual number
def check_number(guess, actual, turns):
    if guess > actual:
        print("Too High")
        return turns - 1
    elif guess < actual:
        print("Too Low")
        return turns - 1
    else:
        print("You got it!")

#make a function to set difficulty
def set_difficulty():
    selectlevel = input("select level:Type Easy or Hard ").lower()
    if selectlevel == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
def game():
    print("welcome to  guess the number game")
    #choosing a random between 1 and 100
    actualnumber = randint(1, 100)
    print(f"The answer is {actualnumber}")

    turns = set_difficulty()
   

    #repeat guessing if it is wrong
    guessnumber = 0
    while guessnumber != actualnumber:
        print(f"you have {turns} attempts remaining to guess the number")
        #guess the number
        guessnumber = int(input("Guess the number between 1 and 100: "))

        #check the answer
        turns = check_number(guessnumber, actualnumber, turns)

        if turns == 0:
            print("You dont have anymore attempt remaining. You lose")
            return

game()
    

    