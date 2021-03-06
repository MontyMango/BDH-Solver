from time import sleep


class Solver :
    def __init__(self) :
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
        self.p1 = 0  # An invalid number
        self.p2 = 0  # A serious error occurred
        # used for options (Default settings)
        self.strip = 1      # strips 0x and 0b on Hex and Binary problems
        self.binary255 = 0  # expands binary to 255 if problem is under 255

        self.filefor = []   # settings.txt document to this list
        # open to settings file to save settings
        try :
            self.r = open('settings.txt', 'r')  # reads settings
        except FileNotFoundError :
            print("\'settings.txt\' file wasn't found with the py program. Creating a blank page...\n\n\n")
            sleep(2)
            open('settings.txt', 'x')  # creates settings.txt file if doesn't exist
            self.r = open('settings.txt','r')   # opens and reads a blank settings page
        print("Welcome, what would you like solved today?\n\n",
              "1. Decimal\n 2. Hexadecimal\n 3. Binary\n 9. Options\n 0. Exit")

    def setup(self) :
        try:
            with open('settings.txt','r') as file:  # opens file for reading
                self.filefor = file.read()      # reads file

            if "0=1" in self.filefor :  # Stripped
                self.strip = 1
            else :
                self.strip = 0

            if "1=1" in self.filefor :  # Binary to 255
                self.binary255 = 1
            else :
                self.binary255 = 0


            self.r.close()
            self.menu()
        except:
            print("Resulting to default settings. settings.txt failed to be created.")
            self.menu()

    def Options(self) :
        print("\n\nAnything you want changed?\n(Be sure to exit to save your settings)\n\n")
        if self.strip == 0 :
            print("1. Turn striping on (0X, 0b)")
        else :
            print("1. Turn striping off (0X, 0b)")
        if self.binary255 == 1 :
            print("2. Don't add extra zeroes when binary's less than 255 (_1100000)\n")
        else :
            print("2. Add extra zeroes to binary when it's less than 255 (01100000)\n")
        print("0. Exit\n")

        try :
            inp = int(input("Option#"))
            if inp == 1 :
                if self.strip == 1 :
                    self.strip = 0
                else :
                    self.strip = 1
                self.Options()
            elif inp == 2 :
                if self.binary255 == 1 :
                    self.binary255 = 0
                else :
                    self.binary255 = 1
                self.Options()
            elif inp == 0 :
                self.w = open('settings.txt', 'w')  # writes settings
                self.am = open('settings.txt', 'a')  # appends settings
                if self.strip == 1 :
                    self.w.write("0=1 ")
                elif self.strip == 0 :
                    self.w.write('0=0 ')
                if self.binary255 == 1 :
                    self.am.write("1=1")
                elif self.binary255 == 0 :
                    self.am.write('1=0')
                    self.w.close()
                    self.am.close()
                print("Welcome, what would you like solved today?\n\n",
                      "1. Decimal\n 2. Hexadecimal\n 3. Binary\n 9. Options\n 0. Exit")
                self.menu()
            else :
                print("Put in a correct number please"), self.Options()
        except :
            print("This only accepts numbers")
            self.Options()

    def menu(self) :
        try :
            self.pick = int(input("\nOption #"))
            if self.pick == 1 :
                try :
                    self.a1 = input("Decimal number: ")
                    self.DecimalSolve()
                except :
                    print("Decimal is unavalible...")
                    self.menu()
            elif self.pick == 2 :
                try :
                    self.a2 = input("Hexadecimal number: ")
                    self.DecimalSolve()
                except :
                    print("Hexadecimal is unavalible...")
                    self.menu()
            elif self.pick == 3 :
                try :
                    self.a3 = input("Binary number:")
                    self.DecimalSolve()
                except :
                    print("Binary is unavailable...")
                    self.menu()
            elif self.pick == 9 :
                self.Options()
            elif self.pick == 0 :
                self.Exit()
            else :
                print("Please select another number...")
                self.menu()

        except :
            print("I am sorry, what was that?")
            self.menu()

    def DecimalSolve(self) :
        try :
            if self.a1 != 0 :
                self.path = self.dec
                self.a = self.a1
                self.a1 = 0

            elif self.a2 != 0 :
                self.path = self.hexa
                self.a = self.a2
                self.a2 = 0

            elif self.a3 != 0 :
                self.path = self.bina
                self.a = self.a3
                self.a3 = 0
        except :
            print("Number wasn't used... Returning to menu")
            self.menu()

        try :  # decimal
            self.d = int(self.a, self.path)
        except ValueError :
            self.d = "Invalid number"
            self.p1 = 1
        except :
            self.d = "Error has occurred"
            self.p2 = 1

        try :  # hexadecimal
            self.h = int(self.a, self.path)
            self.h = hex(self.h)
            if self.strip == 1 :
                self.h = self.h.strip('0x')
            self.h = self.h.upper()
        except ValueError :
            self.h = "Invalid number"
            self.p1 = 1
        except :
            self.h = "Error has occurred"
            self.p2 = 1

        try :  # binary
            self.b = int(self.a, self.path)
            if self.binary255 == 1:
                if self.strip == 1:
                    self.b = format(self.b,'08b')
                else:
                    self.b = format(self.b,'#08b')
            else:
                self.b = bin(self.b)
                if self.strip == 1:
                    self.b = self.b.lstrip("0b")
        except ValueError :
            self.b = "Invalid number"
            self.p1 = 1
        except :
            self.b = "Error has occurred"
            self.p2 = 1

        if self.p1 == 1 :  # if an ultimate error occurred
            print("You didn't put in a valid number, what the heck.")
            self.p1 = 0
        elif self.p2 == 2 :
            print("A very serious error has occurred, what have you done?")
            self.p2 = 0
        else :
            print("\nAnswers\nDecimal: ", self.d, "\nHexadecimal: ", self.h, "\nBinary: ", self.b)
        sleep(2)
        self.Continue()

    def Continue(self) :
        print("\nWould you like to solve another problem?\n")
        print("[y or n]\n")
        self.answer = input(">")
        if self.answer == 'y':
            print("\n\nHere's the delicious menu again \n 1. Decimal\n 2. Hexadecimal"
                  "\n 3. Binary\n 9. Options\n 0. Exit")
        self.answer = input("\nWould you like to solve another problem?\n[y or n]\n>")
        if self.answer == 'y' :
            print("\n\nHere's the delicious menu again \n 1. Decimal\n 2. Hexadecimal\n 3. Binary\n 9. Options\n 0. Exit")
            self.menu()
        elif self.answer == 'n':
            self.Exit()
        else :
            print("\n\nlet me repeat myself...\n\n")
            sleep(1)
            self.Continue()

    def Exit(self):
        print("\n\n\n\n\nThank you for using BHD Solver and goodbye...")
        self.r.close()
        sleep(3)


S = Solver()
S.setup()
