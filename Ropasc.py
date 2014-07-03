# My version of Rock Paper Scissors made using Python

import random
def menu():
    print("1.Rock")
    print("2.Paper")
    print("3.Scissors")
    print("4.Quit")
def clear():
    os.system("clear")
def rounds():        # Asks how many rounds
    rnum = 0
    while rnum%2 == 0 or rnum <= 1:
        try:
            rnum = int(input("How many rounds?!?: "))
        except ValueError:
            print ("Must be an odd number of rounds and more than 1, try again!")
    return rnum
def convert(choice):
    final = ""
    if choice == 1:
        final = "Rock"
    elif choice == 2:
        final = "Paper"
    elif choice == 3:
        final = "Scissors"
    return final
def max():
    wtf = rounds()
    game(wtf)
def game(rounds):
    win = 0
    tie = 0
    lose = 0
    choices = (1,2,3)
    menu()
    for i in range(1,rounds+1):
        ai=random.choice(choices)
        ai_final = convert(ai)
        print("\n","ROUND", i)
        choice = 0
        while choice < 1 or choice > 3:
            try:
                choice = int(input("Choose your weapon: "))
            except ValueError:
                print("Choose a number..")
        final = convert(choice)
        print ("YOU CHOOSE " + final)
        print("[AI]: I Choose ", ai_final)
        if choice == 1 and ai == 3:
            win +=1
            print ("You CRUSH scissors with rock")
        elif choice == 2 and ai == 1:
            win +=1
            print ("You SUFFOCATE rock with paper")
        elif choice == 3 and ai == 2:
            win +=1
            print ("You SHRED paper with scissors")
        elif choice == ai:
            tie +=1
            print ("WHAT?! STALEMATE")
        else:
            lose+=1
            print ("YOU LOST TO", ai_final)
    print ("Rounds won: ", win)
    print ("Rounds lost: ", lose)
    print ("Rounds tied: ", tie)
    max()
    
print ("WELCOME TO THE FIELDS OF JUSTICE, Prepare for battle")
max()
                
                

                
                
                  

                  
                  
            

        
        

    


