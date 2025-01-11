# operations.py: Used to do binary, hexadecimal, and decimal operations

# SOLVING FUNCTIONS
# INTERNAL FILE USE ONLY
def masterSolvingFunction(number, base):
    try:
        decimal = int(str(number), base)
        binary = bin(decimal)
        hexadecimal = hex(decimal)
        return [decimal, binary, hexadecimal]
    except:
        print("An operations error has occured")
        return False

# FORMATTING FUNCTIONS
def formatNumbers(binary, decimal, hexadecimal, binary255, strip):
    # Formats the hexadecimal
    formattedHexadecimal = hexadecimal.strip('0x') if strip else hexadecimal

    # Check if binary needs to be set to 255
    if binary255:
        # When using format() use the decimal number instead of the binary, if you use binary you will get a str() error
        # Source: https://stackoverflow.com/questions/16926130/convert-to-binary-and-keep-leading-zeros#16926357
        formattedBinary = format(decimal, '08b') if strip else format(decimal, '#010b')
    else:
        formattedBinary = binary.lstrip('0b') if strip else binary

    return [decimal, formattedBinary, formattedHexadecimal ]
    
def solveForDecimal(number, binary255, strip):
    decimal, binary, hexadecimal = masterSolvingFunction(number, 10)
    decimal, formattedBinary, formattedHexadecimal = formatNumbers(binary, decimal, hexadecimal, binary255, strip)
    return [decimal, formattedBinary, formattedHexadecimal]

def solveForBinary(number, binary255, strip):
    decimal, binary, hexadecimal = masterSolvingFunction(number, 2)
    decimal, formattedBinary, formattedHexadecimal = formatNumbers(binary, decimal, hexadecimal, binary255, strip)
    return [decimal, formattedBinary, formattedHexadecimal]

def solveForHexadecimal(number, binary255, strip):
    decimal, binary, hexadecimal = masterSolvingFunction(number.upper(), 16)
    decimal, formattedBinary, formattedHexadecimal = formatNumbers(binary, decimal, hexadecimal, binary255, strip)
    return [decimal, formattedBinary, formattedHexadecimal]
