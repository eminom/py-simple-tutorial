


import sys

try:
    f = open('1.py')
    # s = s.readline()
    # i = int(s.strip())
    a = 1/0
except IOError as err:
    print("I/O error: {0}".format(err))
except ValueError:
    print("Could not convert data into integer")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise  # Throw a again