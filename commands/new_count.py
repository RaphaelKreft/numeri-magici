# import necessary modules
import zlib
import gzip
import sys
import os
import datetime
from time import *
import random

from commands import pwd
from commands import cd
# init random-generator
random.seed()

def new_count():
    """
    This function represents the new_count-command

    Args:       -

    Returns:    -
    """
    def normal_counting():
        for i in range(beginning, ending):
            print(str(i) + " of " + str(number_of_files))
            series_of_numbers = generate_series_of_numbers(i)
            print("Init: " + str(series_of_numbers))
            mutations = {}
            mutations[0] = count(series_of_numbers)
            print("calculate...")
            for i in range(1, sequences +1 , 1):
                num_str = toString(mutations[i - 1])
                mutations[i] = count(num_str)
            print("export mutations: " + str(series_of_numbers))
            export_mutations(series_of_numbers, mutations)

    def random_counting():
        for i in range(0, number_of_files):
            print(str(i) + " of " + str(number_of_files))
            series_of_numbers = generate_series_of_numbers(random.randint(0,99999999999999999999))
            print("Init: " + str(series_of_numbers))
            mutations = {}
            mutations[0] = count(series_of_numbers)
            print("calculate...")
            for i in range(1, sequences +1 , 1):
                num_str = toString(mutations[i - 1])
                mutations[i] = count(num_str)
            print("export mutations: " + str(series_of_numbers))
            export_mutations(series_of_numbers, mutations)

    # get informations and parameters for counting
    while True:
        Name = input("Chose a name for this Counting: ")
        print("Ordner für Zählung wird erzeugt..")
        try:
            os.mkdir(Name)
            cd.change_directory(str(Name))
            os.mkdir("data")
            break
        except IOError:
            print("This directory already exists!")
            continue
    print("Entering directory...")
    cd.change_directory("data")
    kindofcounting = input("How you want to count(normal, random): ")
    while True:
        if kindofcounting == "normal":
            beginning = int(input("Beginning of the counting-ambit: "))
            ending = int(input("Ending of the counting-ambit: "))
            number_of_files = ending - beginning
            break
        elif kindofcounting == "random":
            nums = input("How many random-numbers: ")
            number_of_files = int(nums)
            break
        else:
            print("This is no mode!")
            continue
    print("You want to count " + str(number_of_files) + " Numbers!")
    sequences = int(input_number_of_sequences())

    #counting
    t_start = clock()
    if kindofcounting == "normal":
        normal_counting()
    elif kindofcounting == "random":
        random_counting()
    t_end = clock()
    t = t_end - t_start
    print("")
    print("**********")
    print("   Done   ")
    print("**********")
    print("")
    print("counted " + str(number_of_files) + " files in   " + str(t) + " sec")
    print("left data-directory...")
    print("")
    os.chdir("..")
    pwd.print_working_directory()


def export_mutations(series_of_numbers, mutations):
    """
    Write the mutations in a File

    Args:       series_of_numbers   series_of_numbers to export
                mutations           mutations to export

    Returns:    -
    """
    Filename = str(series_of_numbers)  + ".dat.gz"
    File = gzip.open(str(Filename), "wb")
    # Write the header of the File
    File.write(bytes("# Number: " + series_of_numbers + "\n", "utf-8"))
    File.write(bytes("# Date: " + str(datetime.datetime.now()) + "\n", "utf-8"))
    File.write(bytes("# Encoding:   utf-8\n", "utf-8"))
    # generate export-string
    export_string = ''
    for key,val in mutations.items():
        export_string = export_string + str(key).rjust(2, ' ') + ":" + toString(val) + "\n"
    # write and close File
    File.write(bytes(export_string,"utf-8"))
    File.close()


def generate_series_of_numbers(given_number ,target_length = 20):
    """
    This function generates a series_of_numbers to count.

    Args:       -

    Returns:    series_of_numbers   the generated series_of_numbers
    """
    # hier noch schauen ob es zu fehlern führt, wenn Zahl größer al 20stellen ist.
    if given_number < target_length:
        series_of_numbers = str(given_number).rjust(target_length, '0')
        return str(series_of_numbers)
    else:
        return str(given_number)


def input_number_of_sequences():
    """
    This function call up the wanted number of sequences

    Args:       -

    Returns:    sequences   The entered number of sequences
    """
    sequences = input("How many sequences you want to count:")
    return int(sequences)


def count(series_of_numbers):
    """
    This function counts the digits of a series of numbers and return a new
    series of numbers.(Look and say sequence)

    Args:       series_of_numbers     the series of numbers to count

    Returns:    counter               the generated series_of_numbers
    """
    # init counter-array
    counter = []
    for i in range(0,10):
        counter[i] = 0
    # count digits
    for substr in series_of_numbers:
        counter[int(substr)] = counter[int(substr)] + 1

    return counter


def toString(liste):
    """
    This function converts a list into a String

    Args:       list    The list to convert

    Returns:    string  The generated String
    """
    string = ''
    for i in range(0,10):
        string = string + str(liste[i]).rjust(2,'0')
    return string
