# operations.py: Used to do binary, hexadecimal, and decimal operations

# SOLVING FUNCTIONS
# INTERNAL FILE USE ONLY
def masterSolvingFunction(number, base):
    decimal = int(str(number), base)
    binary = bin(decimal)
    hexadecimal = hex(decimal)
    return [decimal, binary, hexadecimal]
    
def solveForDecimal(number):
    return masterSolvingFunction(number, 10)

def solveForBinary(number):
    return masterSolvingFunction(number, 2)

def solveForHexadecimal(number):
    return masterSolvingFunction(number.upper(), 16)


# FORMATTING FUNCTIONS
# def hexadecimalFormat():

# def binaryFormat():

