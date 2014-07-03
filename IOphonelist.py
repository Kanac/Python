A program that utilises dictionies are filoe I/O to act as a phone list
def print_phone(numbers):
    print ("Telephone numbers:")
    for k, v in numbers.items():
        print("Name: ", k, "\tPhone Number: ", v)
    print ()
def add_phone(phonelist, name, number):
    phonelist[name] = number
def remove_phone(phonelist, name):
    if name in phonelist:
        del phonelist[name]
    else:
        print ("No such person")
def lookup_phone(phonelist, name):
    if name in phonelist:
        print ("Name: ", name, "Phone: ", phonelist[name])
    else:
        print ("No such person")
def save_numbers(numbers, filename):
    out_file = open(filename, "wt")
    for k, v in numbers.items():
        out_file.write(k ,",", v, "\n")
    out_file.close()
    
def load_numbers(numbers, filename):
    in_file = open(filename, "rt")
    while True:
        in_line = in_file.readline()
        if not in_line:
            break
        in_line = in_line[:-1]
        name, number = in_line.split(",")
        numbers[name] = number
    in_file.close()
            
    
def print_menu():
    print('1. Print Phone Numbers')
    print('2. Add a Phone Number')
    print('3. Remove a Phone Number')
    print('4. Lookup a Phone Number')
    print('5. Load numbers')
    print('6. Save numbers')
    print('7. Quit')
    print()
phonelist = {}
choice = 0
print_menu()
while True:
    choice = int(input("Select an option(1-7): "))
    if choice == 1:
        print_phone(phonelist)
    elif choice == 2:
        name = input("Name of person: ")
        number = int(input("Phone number: "))
        add_phone(phonelist, name, number)
    elif choice == 3:
        name = input("Name of person: ")
        remove_phone(phonelist, name)
    elif choice == 4:
        name = input("Name of person: ")
        lookup_phone(phonelist, name)
    elif choice == 5:
        filename = input("Filename to load: ")
        load_numbers(phonelist, filename)
    elif choice == 6:
        filename = input("Filename to save: ")
        save_numbers(phonelist, filename)
    elif choice == 7:
        break
    else:
        print_menu()
print ("Goodbye")
                
        
            

    
        
