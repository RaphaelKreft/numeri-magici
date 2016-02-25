# -*- coding: utf-8 -*-

"""cd.py:    This file is a Part of the "Ziffernzählmaschiene-Simulation"
                It Contains a function to change the directory. Its a module, that will be
                imported by the shell.py.
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
#import commands
from commands import pwd

def change_directory(directory):
    """
     Tis function try to enter a dirctory

    Args:       directory    name of the directory you want to enter

    returns:    -
    """
    try:
        os.chdir(str(directory))
    except IOError:
        print("This directory doesnt exist!")
        pwd.print_working_directory()
        return 1
    pwd.print_working_directory()
    return 0
