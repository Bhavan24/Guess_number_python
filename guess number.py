import random
hidden = random.randint(1,20)
guesses_taken = 0

while guesses_taken < 5:
    guess = int (input("Enter a number (between 1 to 20): "))
    guesses_taken += 1
    while guess != hidden:
        if guess < hidden:
            print("Guess was too low")
            break
        if guess > hidden:
            print("Guess was too high")
            break
        guess = int (input("Enter a number (between 1 to 20): "))
        guesses_taken += 1
        if guess == hidden:
            break
    if guess == hidden:
            break
if guess == hidden:
    print("You Are Correct, Answer is: ",hidden,"\nGuesses Taken: ",guesses_taken)
else:
    print("You Are Wrong, Answer is: ",hidden,"\nGuesses Taken: ",guesses_taken)