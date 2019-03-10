from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time

m = PyMouse()
k = PyKeyboard()

buddyX, buddyY = (-1691, 399)
selectX, selectY = (-852, 495)
startX, startY = (431, 229)

m.move(buddyX, buddyY)
m.click(buddyX, buddyY, button=1, n=2)
m.move(selectX, selectY)
time.sleep(5)
#m.click(selectX, selectY, button=1, n=2)
m.move(startX, startY)
time.sleep(4)
#m.click(startX, startY, button=1, n=2)

'''
print('开始')
m.move(buddyX, buddyY)
m.click(buddyX, buddyY, button=1)
print('单击')
time.sleep(5)

m.click(buddyX, buddyY, button=1, n=2)
print('双击')
time.sleep(15)

m.move(selectX, selectY)
m.click(selectX, selectY, button=1)
print('选择按钮')
time.sleep(5)

m.click(selectX, selectY, button=1)
print('选择按钮')
time.sleep(45)

m.click(startX, startY, button=1)
print('开始')
'''
