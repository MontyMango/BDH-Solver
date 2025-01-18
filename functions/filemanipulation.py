# filemanipulation.py: Used to read from and write to the save file.
SETTINGS_FILE_PATH = '../.settings'

# Startup sequence for the program's file system
def fileStartUp():
    # See if the file exists, if it doesn't create the file.
    try:
        file = open(SETTINGS_FILE_PATH, 'r')
    except FileNotFoundError:
        file = open(SETTINGS_FILE_PATH, 'x')
        saveSettings(0, 0)
    file.close()
    return readSettings()

# Reads the settings from the file
def readSettings():
    # From settings.py
    def ifInFile(value, file):
        return True if value in file else False

    with open(SETTINGS_FILE_PATH, 'r') as file:
        settingsFile = file.read()

    # Stripped settings
    stripped = ifInFile("0=1", settingsFile)

    # Binary to 255
    binary255 = ifInFile("1=1", settingsFile)
    return [ stripped, binary255 ]

# Saves settings from the program to the file
def saveSettings(stripSetting, binary255Setting):
    def convertIntoDigit(value):
        return 1 if value else 0

    stripped = convertIntoDigit(stripSetting)
    binary255 = convertIntoDigit(binary255Setting)

    try:
        fileWrite = open(SETTINGS_FILE_PATH, 'w')       # Used for adding the first setting
        fileAppend = open(SETTINGS_FILE_PATH, 'a')      # Used for adding the rest of the settnigs

        # Stripping settings
        fileWrite.write("0=" + str(stripped))

        # Binary 255 settings
        fileAppend.write(" 1=" + str(binary255))

        fileWrite.close()
        fileAppend.close()

    except FileNotFoundError:
        print("\n! - The .settings file has been moved or deleted! Your settings has not been saved to the .settings file.")

    except PermissionError:
        print("\n! - You do not any permissions to save to the file! Your settings have not been saved to the .settings file.\n")
        
    except:
        print("\n! - An issue has occurred during saving! Your settings have not been saved to the .settings file.\n")

    return True
