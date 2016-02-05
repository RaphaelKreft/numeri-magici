
import zlib
import gzip
import os

def show():
    """
    This function reads all Data of a File and prints it.

    Args:       -

    Returns:    -
    """
    filename = input("Filename: ")
    if os.path.exists(filename):

        if filename.endswith(".dat.gz"):
            File = gzip.open(str(filename),"rb")
            Data = File.read()
            print(Data)

        elif filename.endswith(".txt") or filename == "Result":
            File = open(str(filename), "r")
            Data =  File.read()
            print(Data)
        else:
            print("Dies ist keine Datei")
    else:
        print("Diese Datei existiert nicht")
