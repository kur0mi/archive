import utf9
with open("aaa", "rb") as f:
    ss = f.read()

with open("2", "w") as f:
    f.write(utf9.utf9decode(ss))

