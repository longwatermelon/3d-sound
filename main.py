import math
import os

def rotate(origin, point, angle):
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy

def main():
    maxvol = float(input("Max volume percentage: "))

    orig = (0.0, 0.0)
    point = (10.0, 0.0)

    while True:
        point = rotate(orig, point, math.radians(1))
        px, py = point
        px += 10.
        # py += 10.
        # print(px, py)
        right = abs(px) / 20.
        left = 1. - right

        maxvol_adjusted = (maxvol / 1.5) + (1. - (abs(py) / 10.)) * (maxvol * 0.333)
        left *= maxvol_adjusted
        right *= maxvol_adjusted

        left = int(left)
        right = int(right)

        cmd = f"amixer sset Master {left}%,{right}% > /dev/null"
        print(cmd)
        os.system(cmd)

main()

