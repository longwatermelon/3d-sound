import math
import os

def adjust_volume(angle: float, maxvol: float):
    x = math.cos(angle)

    left = (1 - x) / 2.
    right = (1 + x) / 2.

    change = (1 - (abs(math.sin(angle)) - 0.9)) * (maxvol / 2) + (maxvol / 2)
    left *= change
    right *= change

    left = int(left)
    right = int(right)

    cmd = f"amixer sset Master {left}%,{right}% > /dev/null"
    print(cmd)
    os.system(cmd)

def main():
    maxvol = float(input("Max volume percentage: "))
    angle = 3.14 / 2.

    while 1:
        adjust_volume(angle, maxvol)
        angle += 0.01

main()

