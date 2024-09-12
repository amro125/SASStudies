import numpy as np
import math
import time
# from xarm.wrapper import XArmAPI
import SASutils

if __name__ == "__main__":
    xarm = SASutils.robotsUtils("192.168.1.234",True)
    points = [ [[10,10,10,0,0,0],2,0], [[20,20,20,5,3,2],3,0],[[30,30,30,5,3,2],3,1]]
    xarm.p2pTraj(points)
    # print(trajectory[0])  
