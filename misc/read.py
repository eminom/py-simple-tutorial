#! python
import os
import sys

def readFile(path):
    print("Reading {0}".format(path))
    with open(path) as fin:
        lines = fin.readlines()
        print(''.join(lines))   # The separator is already there.

if __name__ == "__main__":
    if len(sys.argv) > 1:
        readFile(sys.argv[1])

    
