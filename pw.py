pw = "hue"
count = 3
print ("You have 3 tries")
attempt = input("Guess my name: " )
while count >1 and attempt != pw:
    count = count - 1
    print(count, " tries left")
    attempt = input("Guess my name: " )
if count >=1 and attempt == pw:
    print ("You win with", count, "tries left")
