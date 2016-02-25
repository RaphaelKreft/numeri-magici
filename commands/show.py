# -*- coding: utf-8 -*-

"""show.py:    This file is a Part of the "Ziffernzählmaschiene-Simulation"
               It Contains a function to show all contents of Files .It will be imported by the shell.py.
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
import gzip
import os


def show():
    """
    This function reads all Data of a File and prints it.

    Args:       -

    Returns:    -
    """
    filename = str(input("Filename: "))
    if os.path.exists(filename):

        if os.path.isfile(filename):

            print(str(filename) + " exists!")
            if filename.endswith(".dat.gz"):
                file = gzip.open(str(filename), "rb")
                for line in file:
                    print(line.rstrip())
                print("\n\n**********Done**********")
                return
            elif filename.endswith(".txt") or filename == "Result":
                file = open(str(filename), "r")
                for line in file:
                    print(line.rstrip())
                print("\n\n**********Done**********")
                return
            else:
                print("This File isn't compatible")

        elif os.path.isdir(filename):
            print(str(filename) + " is a directory")

        elif os.path.islink(filename):
            print(str(filename) + " is a systemlink")
    else:
        print(str(filename) + " doesnt exist!")
    return
