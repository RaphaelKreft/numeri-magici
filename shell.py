#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
Author: Raphael Kreft
Datum: 23.10.2015
Version: 0.3

Support: kreft@phaenovum.de
"""

import os
import time
import sys
#import commands for Shell
from commands import new_count
from commands import list
from commands import cd
from commands import analyse
from commands import show
from commands import pwd

def main():
    """
    This function is the main-function of the Shell

    Args:           -

    Returns:        -
    """
    print("Starting Shell...")
    print("Enter countings-directory")
    try:
        cd.change_directory("countings")
    except IOError:
        print("countings-directory doesnt exist, make directory...")
        os.mkdir("countings")
        cd.change_directory("countings")
    # real shell in a loop
    print("'help' to show all commands")
    while True:
        Befehl = input("--> ")
        if Befehl == "help":
            print("new count        makes a new count")
            print("list             lists all files in a directory")
            print("cd               enters a directory")
            print("analyse          starts the analyse")
            print("show             Shows the contents of a file")
            print("pwd              prints the working directory")
            print("exit             leaves the Shell")
        elif Befehl == "new count":
            new_count.new_count()
            continue
        elif Befehl == "list":
            list.list()
            continue
        elif Befehl == "cd":
            directory = input("which directory: ")
            cd.change_directory(directory)
            continue
        elif Befehl == "analyse":
            analyse.analyse()
            continue
        elif Befehl == "show":
            show.show()
            continue
        elif Befehl == "pwd":
            pwd.print_working_directory()
            pass
            continue
        elif Befehl == "exit":
            print("leaving Shell...")
            #break loop to leave Shell
            break
        else:
            print("Thats no command, enter 'help'")
            continue
    sys.exit(0)

if __name__ == '__main__':
    main()
