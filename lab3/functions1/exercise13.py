#Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen 
# between 1 and 20. 
from random import randint
def guessnumber():
    print("Hello! What is your name?")
    name = input()
    print(f"Well,{name}, I am thinking of a number between 1 and 20")
    number = randint(1,20)
    guesses=0
    while True:
        usrnum=int(input("Take a guess: "))
        guesses+=1
        if usrnum==number:
            print(f"Good job, {name}! You guessed in {guesses} guesses!")
            break
        if number>usrnum:
            print("You guess too low")
        if number<usrnum:
            print("You guess to high")

guessnumber()