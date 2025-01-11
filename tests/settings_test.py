# settings_test.py: Tests the settings page
import pytest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../functions')))

# Imports from the file
from settings import toggleSetting, toggleStriping, toggleBinary255

# If this works, the rest is supposed to work
def test_toggleSetting():
    assert toggleSetting(False) == True
    assert toggleSetting(True) == False

def test_toggleStriping():
    assert toggleStriping(False) == True
    assert toggleStriping(True) == False

def test_toggleBinary255():
    assert toggleBinary255(False) == True
    assert toggleBinary255(True) == False