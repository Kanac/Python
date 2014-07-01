tries = 0
number=int(input("Input a number:"))
print()
guess=int(input("guess the number:"))
if guess==number:
    print("correct!")
while guess!=number:
        tries = tries + 1
        if tries >= 3:
            print ("This must be a complicated number..")
        if guess>number:
                print("Too high!")
        elif guess<number:
                print("Too low!")
        guess=int(input("Guess again:"))
if guess==number:
    print ("Correct!")
              
