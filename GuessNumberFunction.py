import random
def guessNumber(num):
    randNum = random.randrange(0, 20)
    if num != randNum:
        if num < randNum:
            print("Oops! your number is just a little less than the actual number. Try again")
        elif num > randNum:
            print("Oops! your number is just a little higher than the actual number. Try again")
    else:
        print("You guessed rightly, yipee!")

userNum = int(input("Guess: "))
guessNumber(userNum)