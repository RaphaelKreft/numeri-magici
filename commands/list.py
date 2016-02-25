# -*- coding: utf-8 -*-

"""list.py:    This file is a Part of the "Ziffernzählmaschiene-Simulation"
                It Contains a function to show all Files and Directories in the
                working directory. It will be imported by the shell.py.
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
import glob
import os
# import commands
from commands import pwd

def list():
    """
    This function shows all Text and Compressed-Files in your Directory

    Args:       -

    Returns:    -
    """
    # init lists to save items in
    textfilelist = []
    compressedfilelist = []
    dirlist = []

    items = glob.glob("*")
    for item in items:
        if os.path.islink(item):
            print(str(item) + "is a systemlink")
        elif os.path.isdir(item):
            dirlist.append(item)
        elif os.path.isfile(item):
            if item.endswith(".txt") or item == "Result":
                textfilelist.append(item)
            elif item.endswith(".dat.gz"):
                compressedfilelist.append(item)

    print("#####Text-Files(.txt)#####")
    for file in textfilelist:
        print(str(file) + "\n")
    print("#####Compressed-Files(.dat.gz)#####")
    for file in compressedfilelist:
        print(str(file) + "\n")
    print("#####Directories#####")
    for dir in dirlist:
        print(str(dir) + "\n")
    pwd.print_working_directory()
    return
