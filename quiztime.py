questions_answers = [["What is the max level of a Super saiyan?: ", "18"],
                     ["What is the best item in the game?: ", "Boots"],
                     ["Who is numero un?: ", "Mordekaiser"]]
def menu():
    print ("1. Take the test")
    print ("2. Review questions and answers")
    print ("3. View menu")
    print ("4. Quit")
def test(questions):
    index = 0
    right = 0
    while index < len(questions_answers):
        user_answer = input(questions_answers[index][0])
        if user_answer == questions_answers[index][1]:
            print ("Correct")
            right = right + 1
        else:
            print ("Incorrect")
        index = index + 1
    print ("You got", right, "out of ", len(questions_answers), ". That's", right/len(questions_answers) * 100,"%!")
menu()
choice = 0
while choice != 4:
    print ("\n")
    choice = int(input("Select an option from the menu: "))
    try:
        if choice == 1:
            test(questions_answers)
        elif choice == 2:
            for x in range(len(questions_answers)):
                print (questions_answers[x][0],questions_answers[x][1],"\n")
        elif choice == 3:
            menu()
        elif choice != 4:
            print ("Not a valid option")           
    except ValueError:
        print ("Not a valid option")
print ("See ya later m'lady")

