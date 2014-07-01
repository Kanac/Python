print
def hello():
    print('Hello!')
 
def area(width, height):
    return width * height
def tri(base, height):
    return base * height /2

def circumference(radius):
    return 3.14 * radius**2
 
def print_welcome(name):
    print('Welcome,', name)
 
def positive_input(prompt):
    number = float(input(prompt))
    while number <= 0:
        print('Must be a positive number')
        number = float(input(prompt))
    return number

def print_options():
    print ("'p' to see menu")
    print ("'r' to find the area of a rectangle")
    print ("'c' to find the area of a circle")
    print ("'s' to find the area of a sqaure")
    print ("'t' to find the area of a triangle")
    
name = input('Your Name: ')
hello()
print_welcome(name)
print()
choice = "p"
while choice != "q":
    if choice == "p":
        print_options()
    elif choice == "r":
        print('To find the area of a rectangle,')
        print('enter the width and height below.')
        print()
        w = positive_input('Width: ')
        h = positive_input('Height: ')
        print('Width =', w, 'Height =', h, 'so Area =', area(w, h))
    elif choice == "c":
        print('To find the area of a circle,')
        print('enter the radius below.')
        print()
        r = positive_input('Radius:')
        print ("Radius =", r, "so Circumference =" , circumference(r))
    elif choice == "t":
        print('To find the area of a triangle,')
        print('enter the base and height below.')
        print()
        b = positive_input('Base:')
        h = positive_input("Height:")
        print ("Base =", b, "Height =", h, "so Area =" , tri(b,h))
    elif choice == "s":
        print('To find the area of a square,')
        print('enter the width and length below.')
        print()
        w = positive_input('Width: ')
        l = positive_input('Length: ')
        print('Width =', w, 'Length =', l, 'so Area =', area(w, l))
    else:
        print ("That's not a valid option, Summoner")
        print_options()
    print ()
    choice = input("Input:")
        
   
        
