max_points = [25, 25, 50, 25, 100]
assignments = ['hw ch 1', 'hw ch 2', 'quiz   ', 'hw ch 3', 'test']
students = {'#Max': max_points}
 
def print_menu():
    print("1. Add student")
    print("2. Remove student")
    print("3. Print grades")
    print("4. Record grade")
    print("5. Print Menu")
    print("6. Exit")
def print_all_grades():
    for i in range(len(assignments)):
        print ('\t', assignments[i], end= '')
    print ()
    keys = list(students.keys())
    keys.sort()
    for i in keys:
        print (i, '\t', end = '')
    grades = students[i]
    print_grades(grades)
def print_grades(grades):
    for i in range(len(grades)):
        print (grades[i],'\t'"        ", end= '')
        
choice = 0

while choice != "6":
    print_menu()
    choice = input("Select an option (1-6): ")
    if choice == "1":
        print()
        name = input("What is the name of the student you wish to add?: ")
        students[name] = [0] * len(max_points)
    if choice == "2":
        print()
        name = input("What is the name of the student you wish to remove?: ")
        if name in students:
            del students[name]
        else:
            print (name, " not found")
    if choice == "3":
        print_all_grades()
    if choice == "4":
        name = input("Who do you want to record grades for?: ")
        if name in students:
            print("Type in the number of the grade to record")
            print("Type a 0 (zero) to exit")
            grades = students[name]
            for i in range(len(assignments)):
                print (i +1,'\t', assignments[i], end= '')
            print()
            print_grades(grades)
            

                
            

        

