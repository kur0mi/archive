import binascii
data = open("flag.png", "rb").read()
#print(data)
h = binascii.b2a_hex(data)
#print(h)
h = "8950"+h[4:]
fix_data = binascii.a2b_hex(h)

with open("outut.png", "wb") as f:
    f.write(fix_data)
