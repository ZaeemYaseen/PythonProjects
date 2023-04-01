import time   #pausing the console
import random #for random number
from colorama import Fore, Style # for coloring text
import re # for checking if name string contains number or special character
import os # for clearing screen

#function for clearing console
def clear():
    os.system('cls')

#function for display Welcome to the game and creator of program name
def greetin():
    print("\n")
    print("\t\t*************************************************************************************************************************************")
    print("\t\t*                                _____           _____   _____   ___     ___   _____     _____ _____  _____                         *")
    print("\t\t*                |           |  |       |       |       |     | |   |   |   | |               |      |     |                        *")
    print("\t\t*                |           |  |_____  |       |       |     | |   |___|   | |_____          |      |     |                        *")
    print("\t\t*                |     |     |  |       |       |       |     | |           | |               |      |     |                        *")
    print("\t\t*                |_____|_____|  |_____  |_____  |_____  |_____| |           | |_____          |      |_____|                        *")
    print("\t\t*                 _____ _____            _____      ___             ___     ___    _____    _____   _____                           *")
    print("\t\t*                      |       |     |  |          |   |  |     |  |   |   |   |  |     |  |       |     |                          *")
    print("\t\t*                      |       |_____|  |_____     |   |  |     |  |   |___|   |  |_____|  |_____  |_____|                          *")
    print("\t\t*                      |       |     |  |          |   |  |     |  |           |  |     |  |       | *                              *")
    print("\t\t*                      |       |     |  |_____     |   |  |_____|  |           |  |_____|  |_____  |   *                            *")
    print("\t\t*   _____                _____   _____    _____   _____ _____   ___    _____         _____       _____    ___     ___    _____      *")
    print("\t\t*  |           |     |  |       |        |             |       |   |  |             |           |     |  |   |   |   |  |           *")
    print("\t\t*  |   __ __   |     |  |_____  |_____   |_____        |       |   |  |   __ __     |   __ __   |_____|  |   |___|   |  |_____      *")
    print("\t\t*  |     |  |  |     |  |             |        |       |       |   |  |     |  |    |     |  |  |     |  |           |  |           *")
    print("\t\t*  |_____|  |  |_____|  |_____   _____|   _____|  _____|_____  |   |  |_____|  |    |_____|  |  |     |  |           |  |_____      *")
    print("\t\t*************************************************************************************************************************************")

    print("\n\n")
    print("\t\t _________________________________________ ")
    print("\t\t|                                         |")
    print("\t\t| ==>  CREATED BY ZAEEM MUHAMMAD YASEEN.  |")
    print("\t\t|_________________________________________|")

#function for asking options from user
def options():
    print(Fore.BLUE,"\n 1)     NEW GAME.")
    print(" 2)     SCORES.")
    print(" 3)     EXIT.")
    while(1):
        #if user enters invalid input go to except block
        try:
            print(Fore.BLUE)
            choice = input("\nENTER YOUR CHOICE: ")
            given = int(choice)
            clear()
            break
        except:
            print(Fore.RED, "PLEASE ENTER A VALID CHOICE.", Style.RESET_ALL)
    return given

#function for asking player name
def info():
    while(1):
        print(Fore.BLUE,"ENTER YOUR NAME: ")
        name = input()
        #check if player enters number or special symbol in his name
        if (bool(re.search('^[a-zA-Z]*$',name))==True):
            return name
        else:
            print(Fore.RED,"NAME CAN'T CONTAINS ANY NUMBERS OR SPECIAL CHARACTERS.",Style.RESET_ALL)

#working of game
def game():
    name = info()
    count = 0
    #select random number from 1 - 10
    val = random.randrange(1, 10)
    print(Fore.YELLOW,"\nSYSTEM HAS SELECTED THE NUMBER IN RANGE(1 - 10).\n")
    while (1):
        # check if user entered a valid number else go to except block
        try:
            print(Fore.BLUE,"GUESS THE NUMBER: ")
            guess = int(input())
        except:
            print(Fore.RED, "PLEASE 'ENTER' A VALID NUMBER.")
            #jump to next iteration
            continue
        # if user guess right
        if guess == val:
            print(Fore.GREEN,"\n==>  CONGRATUALATIONS YOU GUESSED IT RIGHT AFTER " + str(count) + " turn.")

            #storing name and turn count in the file
            file2 = open('record.txt','a')     #opening the file
            store = str(count) + "\t" + str(name) + "\n"
            file2.write(store)    #writing in the file
            file2.close()    #closing the file

            input("PRESS 'ENTER' KEY TO GO TO MENU.")
            clear()
            break
        #if user number < system number
        elif guess < val:
            print(Fore.CYAN,"Too low habibi go higher.")
        # if user number > system number
        elif guess > val:
            print(Fore.CYAN,"Too high habibi go lower.")
        #counting number of turns
        count += 1

#display score history
def record():
    #opening file
    file1 = open("record.txt")
    print(Fore.YELLOW,"------- -------")
    print("| TURNS |  NAME  |")
    print(" ------- ------- ")
    #iterate text from file
    for i in file1:
        print(" ",i,end="")
    print(Style.RESET_ALL)
    file1.close()   #closing file
    input("PRESS ENTER TO RETURN TO MENU")
    clear()    #function call for clearing the console

#if user wants to enter range
# num1 = int(input("Enter one end of the range: "))
# num2 = int(input("Enter other end of the range: "))

#MAIN FUNCTION
greetin()
time.sleep(5)    #pause the console for 5 seconds
clear()
while(1):
    choice = options()
    print(Style.RESET_ALL)
    #if user pressed
    if choice == 1:
        game()
        print(Style.RESET_ALL)
    elif choice == 2:
        record()
    elif choice == 3:
        break
    else:
        print(Fore.Red,"ENTER A NUMBER BETWEEN (1 - 3).")