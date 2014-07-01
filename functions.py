
print
def hello():
    print('Hello!')

def circum(radius):
    return 3.14*r**2
def area(width, height):
    return width * height
 
def print_welcome(name):
    print('Welcome,', name)
 
def rectangle_area(prompt):
    number = float(input(prompt))
    while number <= 0:
        print('Must be a positive number')
        number = float(input(prompt))
    return number

def square_area(prompt):
    number = float(input(prompt))
    while number <= 0:
        print('Must be a positive number')
        number = float(input(prompt))
    return number

def circle_area(prompt):
    number = float(input(prompt))
    while number <= 0:
        print('Must be a positive number')
        number = float(input(prompt))
    return number

name = input('Your Name: ')
hello()
print_welcome(name)
choice = "o"
if choice == "o":
    print()
    print ("'s' to find the area of a square")
    print ("'r' to find the area of a rectangle")
    print ("'c' to find the area of a circle'")
    print ("'o' to go to options ")
    choice = input("Input?: " )
if choice == "a":
    print()
    print ("'s' to find the area of a square")
    print ("'r' to find the area of a rectangle")
    print ("'c' to find the area of a circle'")
    print ("'o' to go to options ")
    choice = input("Input?: " )
    
if choice == "s":
    print('To find the area of a square,')
    print('enter the width and length below.')
    print()
    w = square_area('Width: ')
    l = square_area('Length: ')
    print('Width =', w, 'Height =', l, 'so Area =', area(w, l))
    choice = "a"
if choice == "r":
    print('To find the area of a rectangle,')
    print('enter the width and height below.')
    print()
    w = rectangle_area('Width: ')
    h = rectangle_area('Height: ')
    print('Width =', w, 'Height =', h, 'so Area =', area(w, h))
    choice = "a"
if choice == "c":
    print('To find the area of a rectangle,')
    print('enter the radius below.')
    print()
    r = circle_area('Radius: ')
    print("Radius = ", r, "so Area = ", circum(r))
    choice = "a"
