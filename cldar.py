# Testing the random module and its defined functions

guess = 7867887
number = random.randint(0,99)
while guess != number:
    if guess > number:
        print ("too high")
    if guess < number:
        print ("too low")
print ("You win")
