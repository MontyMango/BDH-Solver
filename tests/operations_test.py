# operations_test.py: Used to test operations
import pytest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../functions')))

# Import from other file
from operations import solveForDecimal, solveForBinary, solveForHexadecimal

def test_decimal():
    assert solveForDecimal(10) == [10, '0b1010', '0xa']

def test_binary():
    assert solveForBinary(1010) == [10, '0b1010', '0xa']

def test_hexadecimal():
    assert solveForHexadecimal('a') == [10, '0b1010', '0xa']