max_points = [25, 25, 50, 25, 100]
assignments = ['hw ch 1', 'hw ch 2', 'quiz   ', 'hw ch 3', 'test']
students = {"#Max": max_points}
def menu():
    print("1. Add student")
    print("2. Remove student")
    print("3. Print grades")
    print("4. Record grade")
    print("5. Print Menu")
    print("6. Exit")
def print_all_grades():
    print('\t', end=' ')
    for i in range(len(assignments)):
        print(assignments[i], '\t', end=' ')
    print ()
    keys = list(students.keys())
    keys.sort()
    for i in keys:
        print (i,end = "")
        print ("\t", end = "")
        grades = students[i]
        print_grades(grades)
def print_grades(grades):
    for i in range(len(grades)):
        print(grades[i],'\t', '\t', end=' ')
    print ()
           
menu()
choice = 0
while choice != "6":
    print ()
    choice = input("Menu Select(1-6): ")
    if choice == "1":
        name = input("1. Add student: ")
        students[name] = [0] * len(max_points)
    if choice == "2":
        name = input("2. Remove student: ")
        if name in students:
            del students[name]
        else:
            print ("No such student")
    if choice == "3":
        print_all_grades()
    if choice == "4":
        name  = input("4. Record grade(enter student name): ")
        if name in students:
            print ("Type in the index of the grade to record")
            print ("Type 0 to exit")
            grades = students[name]
            for i in range(len(assignments)):
                print ("\t", end = "")
                print (i + 1, assignments[i], end ="")
            print ("\t","#Max", end ="")
            for i in students["#Max"]:
                print ("\t", end ='')
                print(i,'\t', end='')
            print ("\t")
            print ("\t", end = "")
            print_grades(grades)
            select = 1111
            while select != -1:
                select = int(input("Which assignment to record?: "))
                select = select -1
                if select in range(len(assignments)):
                    grade = int(input("What mark?: "))
                    grades[select] = grade
                elif select != -1:
                    print("Invalid Grade Number")
        else:
            print ("student not found")
                    
            

            
        
    
            
        
        
    
