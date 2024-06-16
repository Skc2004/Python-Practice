import random
def welcome():
    print("WELCOME TO SNAKE-WATER-GUN GAME\n")
    print("-------------------------------\n")
    print("\n")

def menu():
    print("-: Choose from the following :-\n")
    print("1. Play")
    print("2. Exit")

#def input():
#    q= int(input("Enter your choice :"))
#    return q

def user_choice():
    print("Choose from the following :- \n")
    print("1.Snake\n")
    print("2.Water\n")
    print("3.Gun\n")

def comp_choice():
    return random.randint(1,3)
def game():
    menu()
    #x=input()
    x=int(input("Enter your choice :"))
    if(x==1):
        user_choice()
        #y=input()
        y=int(input("Enter your choice :"))
        z=comp_choice()
        if(y==z):
            print("YOU WON!!!\n")
        else:
            print("YOU LOST!!!\n")
        game()       
    elif(x==2):
        exit()
    else:
        print("Invalid Input!!!")
        game()

welcome()
game()