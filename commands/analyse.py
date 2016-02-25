# -*- coding: utf-8 -*-

"""analyse.py:    This file is a Part of the "Ziffernzählmaschiene-Simulation"
                  It Contains the analyse-functinality. Its imported by the maim-file "shell.py"
                  read the docstring for more Information.
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

#import system-modules
import glob
import gzip
import os
from time import *


def analysis(filename, filepointer):
    """
    This function reads the series of numbers, analyse it and write the results
    in the Result.txt

    Args:       filename    Name of file, to be analysed
                filepointer Reference to File to write

    Returns:    -
    """

    global number

    def figureout_endseq(liste):
        """
        This function finds the normal-series_of_numbers

        Args:   liste   The list of numbers to search for End-seq

        Returns:    k               Run of the endseq
                    standartfolge   endseq which was found

        """
        standartfolge = None
        for i in range(0, len(liste)):
            if liste[i] == liste[i - 1]:
                standartfolge = liste[i]
                k = int(i)
                break
        return str(standartfolge), k

    # read data from file and close it
    f = gzip.open(str(filename), "rb")
    lines = f.readlines()
    f.close()

    numbers = []
    filepointer.write(str(filename) + "\t\t")

    for line in lines:
        if line.startswith(bytes("#", "utf-8")):
            pass
        else:
            line = line.replace(bytes("\n", "utf-8"), bytes("", "utf-8"))
            split = line.split(bytes(":", "utf-8"))

            run = int(str(split[0], "utf-8"))
            # Write first Mutation
            if run == 1:
                filepointer.write(number + "\t\t")
            number = str(split[1], "utf-8")
            numbers.append(number)

    standartfolge, k = figureout_endseq(numbers)
    filepointer.write(str(standartfolge) + "\t\t")
    filepointer.write(str(k) + "\n\n")
    print("finished counting of  " + str(filename))
    return k, standartfolge


def analyse():
    """
    analyse all Files

    Args:       -

    Returns:    -
    """
    print("Starting Analysis...")
    t_start = clock()
    endseq_ratio = [[0 for x in range(2)] for i in range(15)]
    result_file = open("Result", "w")
    result_file.write("\t\t\t\t" + "first Mutation" + "\t\t\t\t" + "Standartfolge" + "\t\t\t" + "Stelle(k)" + "\n\n")
    os.chdir("data")
    files = glob.glob("*.dat.gz")
    files.sort()

    for filename in files:
        k, sf = analysis(filename, result_file)
        if sf == "15030001000100000000":
            endseq_ratio[int(k)][0] += 1
        elif sf == "15020200000100000000":
            endseq_ratio[int(k)][1] += 1

    result_file.write("\tStandartfolgenverteilung\n\nA\tB\n\n")
    for i in range(15):
        result_file.write(str(endseq_ratio[i][0]) + "\t" + str(endseq_ratio[i][1]) + "\n")
    result_file.close()
    t_end = clock()
    t = t_end - t_start
    print("\n*****Done*****")
    print("computing-Time: " + str(t) + " sec")
