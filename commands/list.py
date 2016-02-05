
import glob

def list():
    print("#####Text-Files(.txt)#####")
    files = glob.glob("*.txt")
    for file in files:
        print(str(file) + "\n")
    print("#####Compressed-Files(.dat.gz)#####")
    files = glob.glob("*.dat.gz")
    for file in files:
        print(str(file) + "\n")
