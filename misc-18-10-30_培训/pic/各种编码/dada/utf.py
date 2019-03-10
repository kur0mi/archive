import utf9
import sys

filename = sys.argv[1]
ss = open(filename, "rb").read()
with open("2", "wb") as f:
    f.write(utf9.utf9decode(ss))

