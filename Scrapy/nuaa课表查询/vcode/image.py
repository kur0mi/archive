from PIL import Image
filename = "9440.png"
output = "9440_output.png"
img = Image.open(filename)
img = img.convert("L")  # 灰度处理

# 二值化
threshold = 140     # 阙值
img = img.resize((img.width*2, img.height*2))
for w in range(img.width):
    for h in range(img.height):
        if img.getpixel((w, h)) < threshold:
            img.putpixel((w, h), 0)
        else:
            img.putpixel((w, h), 255)

img.save(output)
