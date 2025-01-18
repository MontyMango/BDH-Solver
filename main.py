import os
import sys
from time import sleep
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), './functions')))
from filemanipulation import fileStartUp, saveSettings
from settings import toggleStriping, toggleBinary255
from operations import solveForDecimal, solveForBinary, solveForHexadecimal, formatNumbers


# TODO: Instead of using global variables, use a class or a function to store the settings?

def startup():
    # Global variables
    global stripingValue, binary255Value
    try:
        stripingValue, binary255Value = fileStartUp()
    # My dev Container encountered this error
    except PermissionError:
        stripingValue, binary255Value = 0, 0
        print("! - The .settings files cannot be created due to permission issues...\nYou won't be able to save your settings for your next session!\n")


def startMenu():
    print("Welcome, what would you like solved today?\n\n",
              "1. Decimal\n 2. Hexadecimal\n 3. Binary\n 9. Options\n 0. Exit")
    pick = int(input("\nOption #"))
    if pick == 1:
        decimalMenu()
    elif pick == 2:
        hexadecimalMenu()
    elif pick == 3:
        binaryMenu()
    elif pick == 9:
        optionMenu()
    elif pick == 0:
        exit()
    else:
        print("Please select another number...")
        startMenu()

def printResults(decimal, binary, hexadecimal):
    print("\nAnswers:\nDecimal: ", decimal, "\nHexadecimal: ", hexadecimal, "\nBinary: ", binary, "\n\n")
    input("Press [enter] to return to the menu\n")
    print ("\033[A\033[A\033[A")        # Removes the previous 3 lines in the console
                                        # Source: https://stackoverflow.com/questions/44565704/how-to-clear-only-last-one-line-in-python-output-console#51388326

def decimalMenu():
    global stripingValue, binary255Value 
    try:
        answer = input("Decimal Number: ")
        decimal, binary, hexadecimal = solveForDecimal(answer, stripingValue, binary255Value)
        printResults(decimal, binary, hexadecimal)
    except:
        print("An invalid decimal value has been inputed!\n")
        sleep(1)
    startMenu()

def binaryMenu():
    global stripingValue, binary255Value 
    try:
        answer = input("Binary Number: ")
        decimal, binary, hexadecimal = solveForBinary(answer, stripingValue, binary255Value)
        printResults(decimal, binary, hexadecimal)
    except:
        print("An invalid binary value has been inputed!\n")
        sleep(1)
    startMenu()

def hexadecimalMenu():    
    global stripingValue, binary255Value 
    try:
        answer = input("Hexadecimal Number: ")
        decimal, binary, hexadecimal = solveForHexadecimal(answer, stripingValue, binary255Value)
        printResults(decimal, binary, hexadecimal)
    except:
        print("An invalid hexadecimal value has been inputed!\n")
        sleep(1)
    startMenu()

def optionMenu():
    global stripingValue, binary255Value 
    print("\n\nAnything you want changed?\n(Be sure to exit to save your settings)\n\n")
    print(stripingValue, binary255Value)
    if stripingValue == False:
        print("1. Turn striping on (0X, 0b)")
    else :
        print("1. Turn striping off (0X, 0b)")
    if binary255Value == True:
        print("2. Don't add extra zeroes when binary's less than 255 (_1100000)\n")
    else :
        print("2. Add extra zeroes to binary when it's less than 255 (01100000)\n")
    print("0. Exit\n")

    pick = int(input("\nOption #"))

    if pick == 1:
        stripingValue = toggleStriping(stripingValue)
        optionMenu()
    elif pick == 2:
        binary255Value = toggleBinary255(binary255Value)
        optionMenu()
    elif pick == 0:
        saveSettings(stripingValue, binary255Value)
        startMenu()
    else:
        print("Number not recognized... Please try again.")
        optionMenu()


while __name__ == '__main__':
    startup()
    startMenu()