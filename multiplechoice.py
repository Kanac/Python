questions_answers = [["10", "5", "16", "18"],     #18 is the right answer(3)
                     ["Boots", "Infinity Edge", "Rabadons", "Leviathian"],      #Boots(0)
                     ["Master Yi","Mordekaiser" ,"Ahri", "Akali"]]        #Mordekaiser(1)
questions=["What is the max level of a Super saiyan?:",
           "What is the best item in the game?:",
           "Who is numero un?: "]
def menu():
    print ("1. Take the test")
    print ("2. Review questions and answers")
    print ("3. View menu")
    print ("4. Quit")
def test(questions_answers, questions):
    index = 0
    right = 0
    while index < len(questions_answers):
        for x in range(len(questions_answers[index])):
            print(x+1, ".",(questions_answers[index][x]))
        user_answer = int(input(questions[index]))
        if index == 0:
            if user_answer == 4:
                right = correct(right)
            else:
                incorrect()
        elif index == 1:
             if user_answer == 1:
                 right = correct(right)
             else:
                incorrect()
        elif index == 2:
            if user_answer == 2:
                 right = correct(right)
            else:
                incorrect()
        index = index + 1
    print ("You got", right, "out of ", len(questions_answers), ". That's", right/len(questions_answers) * 100,"%!")

def incorrect():
    print ("Incorrect")

def correct(right):
        print ("Correct")
        right = right + 1
        return right

menu()
choice = 0
while choice != 4:
    print ("\n")
    choice = int(input("Select an option from the menu: "))
    try:
        if choice == 1:
            test(questions_answers, questions)
        elif choice == 2:
            for x in range(len(questions)):
                print (questions[x])
                if x == 0:
                    print (questions_answers[0][3])
                if x == 1:
                    print (questions_answers[1][0])
                if x == 2:
                    print (questions_answers[2][1])
        elif choice == 3:
            menu()
        elif choice != 4:
            print ("Not a valid option")           
    except ValueError:
        print ("Not a valid option")
print ("See ya later m'lady")
