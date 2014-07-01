questionslist =[["What color is the daytime sky on a clear day?: ", "blue"],
            ["What is the answer to life, the universe and everything?: ", "42"],
            ["What is a three letter word for mouse trap?: ", "cat"]]
def run_test(questions):
    if len(questions) == 0:
        print ("No questions given")
        return
    index = 0
    right = 0
    while index < len(questions):
        if check_questions(questions[index]):
            right = right + 1
        index = index + 1
    print ("You got", right *100/len(questions), "% out of 100%", )

def check_questions(questions):
    question = questions[0]
    answer = questions[1]
    given_answer = input(question)
    if given_answer == answer:
        print ("correct")
        return True
    else:
        print ("incorrect, the answer was", answer)
        return False
def menu():
    print ("1.Take the test")
    print ("2.View the questions and answers")
    print ("3.Quit")
def review():
    count = 0
    while count < len (questionslist):
            a = 0
            print (questionslist[count][a])
            a = 1
            print (questionslist[count][a])
            count = count + 1
menu()
choice = 0
while choice != "3":
    choice = input("Choose an option: ")
    if choice == "1" :
        run_test(questionslist)
    if choice == "2" :
        review()
print ("cya")


    
