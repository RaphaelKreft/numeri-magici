#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""shell.py:    This file is a Part of the "Ziffernzählmaschiene-Simulation"
                It Contains the main-functionality, that means it includes the
                Commandprompt which executes the commands from the loaded modules.
"""

__author__ = "Raphael Kreft"
__copyright__ = "Copyright 2016, numeri magici"
__credits__ = "produced by Raphael Kreft. The Simulation is part of a scientific" \
              "work named 'Die Ziffernzählmaschiene - numeri magici'. The writed" \
              "Version is aviable at: www.bitbuckit.org/Cbetron/numeri_magici"

__license__ = " - "
__version__ = "1.1"
__email__ = "kreft@phaenovum.de"
__status__ = "Production"

# import system-modules
import os
import sys
# import commands for Shell
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
    # check if the countings-directory exists
    print("Starting Shell...")
    print("Enter countings-directory")
    # Try to enter countings directory
    while True:
        success = cd.change_directory("countings")
        if success == 0:
            print("entered dir successful")
            break
        elif success == 1:
            print("error while entering directory, try to make dir..")
            os.mkdir("countings")
            print("successful")
            continue
    # real shell in a loop
    print("'help' to show all commands")
    while True:
        befehl = str(input("--> "))
        if befehl == "help":
            helpstring = "new count        makes a new count\n" \
                         "list             lists all files in a directory\n" \
                         "cd               enters a directory\n" \
                         "analyse          starts the analyse\n" \
                         "show             Shows the contents of a file\n" \
                         "pwd              prints the working directory\n" \
                         "exit             leaves the Shell\n"
            print(helpstring)
        elif befehl == "new count":
            new_count.new_count()
            continue
        elif befehl == "list":
            list.list()
            continue
        elif befehl == "cd":
            directory = input("which directory: ")
            cd.change_directory(directory)
            continue
        elif befehl == "analyse":
            analyse.analyse()
            continue
        elif befehl == "show":
            show.show()
            continue
        elif befehl == "pwd":
            pwd.print_working_directory()
            pass
            continue
        elif befehl == "exit":
            print("leaving Shell...")
            # break loop to leave Shell
            break
        else:
            print("Thats no command, enter 'help'")
            continue
    sys.exit(0)


if __name__ == '__main__':
    main()
