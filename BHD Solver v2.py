from time import sleep

class Solver():
    def __init__(self):
        print("Welcome, what would you like solved today?\n\n",
               "1. Decimal\n 2. Hexadecimal\n 3. Binary")
        # used for menu & self.a is used for DecimalSolve too
        self.pick = 0
        # used for answers
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
        # used for DecimalSolve answers
        self.d = 0
        self.h = 0
        self.b = 0
        # used for DecimalSolve paths
        self.dec = 10
        self.hexa = 16
        self.bina = 2
        # used for problem in DecimalSolve
        self.path = 0
        # used for DecimalSolve for advanced problems
        self.p1 = 0 # An invalid number
        self.p2 = 0 # A serious error occurred

    def menu(self):
        try:
            self.pick = int(input("Option #"))
            if self.pick == 1:
                try:
                    self.a1 = input("Decimal number: ")
                    self.DecimalSolve()
                except:
                    print("Decimal is unavalible...")
                    self.menu()
            elif self.pick == 2:
                try:
                    self.a2 = input("Hexadecimal number: ")
                    self.DecimalSolve()
                except:
                    print("Hexadecimal is unavalible...")
                    self.menu()
            elif self.pick == 3:
                try:
                    self.a3 = input("Binary number:")
                    self.DecimalSolve()
                except:
                    print("Binary is unavalible...")
                    self.menu()
            else:
                print("Please select another number...")
                self.menu()
        except:
            print("I am sorry sir, what was that?")
            self.menu()

    def DecimalSolve(self):
        try:
            if self.a1 != 0:
                self.path = self.dec
                self.a = self.a1
                self.a1 = 0

            elif self.a2 != 0:
                self.path = self.hexa
                self.a = self.a2
                self.a2 = 0

            elif self.a3 != 0:
                self.path = self.bina
                self.a = self.a3
                self.a3 = 0
        except:
            print("Number wasn't used... Returning to menu")
            self.menu()

        try: # decimal
            self.d = int(self.a, self.path)
        except ValueError:
            self.d = "Invalid number"
            self.p1 = 1
        except:
            self.d = "Error has occurred"
            self.p2 = 1

        try: # hexadecimal
            self.h = int(self.a, self.path)
            self.h = hex(self.h)
            self.h = self.h.strip('0x')
            self.h = self.h.upper()
        except ValueError:
            self.h = "Invalid number"
            self.p1 = 1
        except:
            self.h = "Error has occurred"
            self.p2 = 1

        try: # binary
            self.b = int(self.a, self.path)
            self.b = bin(self.b)
            self.b = self.b.lstrip("0b")
        except ValueError:
            self.b = "Invalid number"
            self.p1 = 1
        except:
            self.b = "Error has occurred"
            self.p2 = 1

        if self.p1 == 1: # if an ultimate error occurred
            print("You didn't put in a valid number, what the heck.")
            self.p1 = 0
        elif self.p2 == 2:
            print("A very serious error has occurred, what have you done?")
            self.p2 = 0
        else:
            print("\nAnswers\nDecimal: ",self.d,"\nHexadecimal: ",self.h,"\nBinary: ",self.b)
        sleep(2)
        self.Continue()

    def Continue(self):
        self.answer = input("\nWould you like to solve another problem?\ny or n\n")
        if self.answer == 'y':
            print("\n\nHere's the delicious menu again \n 1. Decimal\n 2. Hexadecimal\n 3. Binary\n")
            self.menu()
        elif self.answer == 'n':
            print("\n\nArrigato mr. program user and goodbye...")
        else:
            print("\n\nlet me repeat myself...\n\n")
            sleep(1)
            self.Continue()


S = Solver()
S.menu()