# operations_test.py: Used to test operations
import pytest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../functions')))

# Import from other file
from operations import solveForDecimal, solveForBinary, solveForHexadecimal

def test_decimal():
    assert solveForDecimal(10, False, False) == [10, '0b1010', '0xa']
    assert solveForDecimal(10, True, False) == [10, '0b00001010', '0xa']        # Only set the binary to 255
    assert solveForDecimal(10, False, True) == [10, '1010', 'a']                # Only strip the left side off
    assert solveForDecimal(10, True, True) == [10, '00001010', 'a']             # Do both

def test_binary():
    assert solveForBinary(1011, False, False) == [11, '0b1011', '0xb']
    assert solveForBinary(1011, True, False) == [11, '0b00001011', '0xb']        # Only set the binary to 255
    assert solveForBinary(1011, False, True) == [11, '1011', 'b']                # Only strip the left side off
    assert solveForBinary(1011, True, True) == [11, '00001011', 'b']             # Do both

def test_hexadecimal():
    assert solveForHexadecimal('c', False, False) == [12, '0b1100', '0xc']
    assert solveForHexadecimal('c', True, False) == [12, '0b00001100', '0xc']       # Only set the binary to 255
    assert solveForHexadecimal('c', False, True) == [12, '1100', 'c']               # Only strip the left side off
    assert solveForHexadecimal('c', True, True) == [12, '00001100', 'c']            # Do both