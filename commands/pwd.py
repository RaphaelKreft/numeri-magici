# -*- coding: utf-8 -*-

"""pwd.py:    This file is a Part of the "Ziffernzählmaschiene-Simulation"
              It Contains a function to printout the working-directory to the
              User. it will be imported by the shell.py, analyse.py, new_count.py
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


def print_working_directory():
    """
    print the working directory

    Args:       -

    Returns:    -
    """
    print("Working Directory: " + str(os.getcwd()))
    return
