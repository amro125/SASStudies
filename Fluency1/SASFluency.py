import numpy as np
import math
import time
# from xarm.wrapper import XArmAPI
import SASutils
import random

# mapping = {'H1': 1, 'M1': 8, 'S1': 2}

types = "HMS"
div = len(types)
per = 4
mapping = {f'{types[i // per]}{i % per + 1}': (i + 1) for i in range(div * per)}
# Autogenerated -> {'H1': 1, 'H2': 2, 'H3': 3, 'H4': 4, 'M1': 5, 'M2': 6, 'M3': 7, 'M4': 8, 'S1': 9, 'S2': 10, 'S3': 11, 'S4': 12}


def main(xarm):
    demos = list(mapping)
    random.shuffle(demos)
    print(demos)
    for demo in demos:
        if 'H' in demo:
            continue
        sound = mapping[demo]
        t = 3 * random.random() + 3
        # delay = random.randrange(0, 5)
        # time.sleep(delay)
        print("Doing trajecrtory " + demo)
        points = [ [[0,35,15,125,-23,0,45],3,0], [[95,15,30,85,-23,-28,45],t,sound],[[0,35,15,125,-23,0,45],3,0]  ]
        xarm.p2pTraj(points)



if __name__ == "__main__":
    simulation = False
    xarm = SASutils.robotsUtils("192.168.1.215",simulation)
    if not simulation:
        xarm.setupBot()
    input("hi")
    main(xarm)

    # sound = -1
    # while sound:
    #     sound = int(input("input sound ID to move: "))
    #     t = 5
    #     if not sound:
    #         break
    #     points = [ [[586,17.9,689,179.6,-71,2],3,0], [[-57,571,456,-160,-39,88],t,sound],[[586,17.9,689,179.6,-71,2],t,sound]] #0,17.6,0,115,0,26  92,11,5,30,30,-18
    #     xarm.p2pTraj(points)
    # print(trajectory[0])  