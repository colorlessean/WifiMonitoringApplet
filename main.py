from Interface.interface import *
from Logic.logic import *
import os

# Function to build temp file that data will be streamed to
def tempFileConstructor(filename):
    open(filename, 'a').close()
    return

# Function to destroy temp file that data was streamed to
def tempFileDestructor(filename):
    # Delete File if flag for deletion has been set
    os.remove(filename)
    return

def main():
    filename = os.curdir + "\\temp.txt"
    print(filename)
    tempFileConstructor(filename)
    logic(filename)
    tempFileDestructor(filename)
    return

# Runs as script remove in final application
main()