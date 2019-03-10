from PIL import Image
from pytesseract import *
im = Image.open("9440.png")
text = image_to_string(im)
print(text)
