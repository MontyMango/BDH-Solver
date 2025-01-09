# settings.py: Used to change settings for the program

def toggleSetting():
    return 0 if currentSetting == 1 else 1      # Interesting one-liner, learned from here: 
                                                # https://stackoverflow.com/questions/41722908/if-statement-to-one-line-with-return#41722943


def toggleStriping(currentStripSetting):
    return toggleSetting(currentStripSetting)

def toggleBinary255(currentBinarySetting):
    return toggleSetting(currentBinarySetting)
