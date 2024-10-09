import numpy as np
import math
import time
# from xarm.wrapper import XArmAPI
import SASutils
import random

mapping = {'H1': 1, 'M1': 8, 'S1': 2}

def main(xarm):
    demos = tuple(mapping)
    for demo in demos:
        # input()
        sound = mapping[demo]
        t = 3 * random.random() + 5
        delay = random.randrange(0, 5)
        time.sleep(delay)
        print("Doing trajecrtory " + demo)
        points = [ [[586,17.9,689,179.6,-71,2],3,0], [[-57,571,456,-160,-39,88],t,sound],[[586,17.9,689,179.6,-71,2],3,0]]
        xarm.p2pTraj(points)



if __name__ == "__main__":
    simulation = True
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