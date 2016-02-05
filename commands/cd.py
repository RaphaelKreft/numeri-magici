
import os

def change_directory(directory):
    """
    Try to enter a dirctory

    Args:       dirctory    the directory you want to enter

    returns:    -
    """
    try:
        os.chdir(str(directory))
    except IOError:
        print("This directory doesnt exist!")
