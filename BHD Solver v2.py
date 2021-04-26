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
        self.yor1 = 0       # y or n at the end == 0, or 1 or 2 at the end == 1
        self.disabled = 0   # if settings.txt cannot be found.
        self.filefor = []   # settings.txt document to this list

        # menus
        self.defmenu = []
        self.menu1 = ['1. Decimal','2. Hexadecimal','3. Binary','9. Options','0. Exit']
        self.menu2 = ['1. Decimal','2. Hexadecimal','3. Binary',
                      '8. Create settings.txt file','9. Temporary settings','0. Exit']

        # exit
        self.ForceExit = 0

        # open to settings file to save settings
        try :
            self.r = open('settings.txt', 'r')  # reads settings
            self.defmenu = self.menu1
            self.summonmenu()
        except FileNotFoundError :
            print("\'settings.txt\' file wasn't found with the py program...\n"
                  "Create a new document by using option #8 while in the menu!\n\n")
            self.defmenu = self.menu2
            self.disabled = 1

        # setup if and for loops, will be tested later
        # self.ifstripped = [self.strip if "0=1" in self.filefor == 1 else 0]
        # self.ifbinary255 = [self.binary255 if "1=1" in self.filefor == 1 else 0]
        # self.ifyor1 = [self.yor1 if "2=1" in self.filefor == 1 else 0]

    def setup(self) :
        try:
            if self.disabled == 1:
                self.summonmenu()
                self.menu()

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

            if self.ForceExit == 1:
                self.Exit()
            self.r.close()
            self.menu()
        except:
            self.Exit()

    def summonmenu(self):
        print("What would you like to solve today?")
        for i in self.defmenu:
            print(i)

    def Options(self) :
        if self.disabled == 0:
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
                if self.disabled == 0:
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
                self.summonmenu()
                self.menu()
            else :
                print("Put in a correct number please"), self.Options()
        except :
            print("This only accepts numbers")
            self.Options()

    def CreateTxt(self):
        if self.disabled == 1:
            print("A text file was created in the ram. Please exit the program to save and make the file.")
            open('settings.txt', 'x')  # creates settings.txt file if doesn't exist
            self.r = open('settings.txt', 'rt')  # opens and reads a blank settings page
            self.menu()
        elif self.disabled == 0:
            print("\n:O There's already a settings file. How are you in here, and what are you doing in here????\n")
            sleep(3)
            self.menu()

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
                    print("Hexadecimal is unavailable...")
                    self.menu()
            elif self.pick == 3 :
                try :
                    self.a3 = input("Binary number:")
                    self.DecimalSolve()
                except :
                    print("Binary is unavailable...")
                    self.menu()
            elif self.pick == 8:
                try:
                    self.CreateTxt()
                except:
                    print("There was an error when creating settings file")
                    self.menu()
            elif self.pick == 9 :
                if self.disabled == 1:
                    print("These settings won't be saved, until you make a new file...\n")
                    self.Options()
                else:
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
                self.h = self.h.lstrip('0x')
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

    def Continue(self) :    # y or 1 function coming soon to this lot!!!
        print("\nWould you like to solve another problem?\n")
        # if self.yor1 == 0:
        print("[y or n]\n")
        # elif self.yor1 == 1:
        #     print("[1.(y) or 2.(n)]")
        self.answer = input(">")
        if self.answer == 'y':
            self.summonmenu()
            self.menu()
        elif self.answer == 'n':
            self.Exit()
        else :
            print("\n\nlet me repeat myself...\n\n")
            sleep(1)
            self.Continue()

    def Exit(self):
        if self.ForceExit == 1:
            print("Exiting...\n(If the application stays open, use option # 0 again. Thanks.)")
        elif self.ForceExit == 0:
            print("\n\n\n\n\nThank you for using BHD Solver and goodbye...")
            if self.disabled == 0:
              self.r.close()
            sleep(2)
            self.ForceExit = 1


S = Solver()
S.setup()
