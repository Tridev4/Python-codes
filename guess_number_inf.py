import random
secretnum=random.randint(1,100)
guessnum=int(input("Guess a number between 1 and 100 inclusive:"))
while guessnum!=secretnum:
    if guessnum<secretnum:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
    guessnum=int(input("Guess a number between 1 and 100 iclusive:"))
print("Congratulations!!!! You guessed the right number.")