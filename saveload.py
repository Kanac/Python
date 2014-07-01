file = open("test.txt", "wt")
file.write("Testing, Testing, I'm just suggesting")
file.write("\n")
file.write("Lol, LOl")
file.close()

nfile = open("test.txt", "rt")
while True:
    text = nfile.readline()
    print(text)
    if not text:
        break

nfile.close()


