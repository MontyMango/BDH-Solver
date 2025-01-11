# fileManipulation_test.py: 
import pytest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../functions')))

# Imports from the file
from filemanipulation import fileStartUp, readSettings, saveSettings

def test_fileStartUp():
    assert fileStartUp() == [False, False]

def test_readSettings():
    assert readSettings() == [False, False]

def test_saveSettings():
    assert saveSettings(0, 0) == True