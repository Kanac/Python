from random import randint
x = randint(0,99)
guess = int(input("Guess the number I'm thinking from 0-99: "))
while guess <= 99 and guess >= 0 and guess != x:
        if guess > x:
            print ("Too high")
        elif guess < x:
            print ("Too low")
        guess = int(input("Guess the number I'm thinking from 0-99: "))
print ("You win")

            
