#!/usr/bin/env python

from __future__ import print_function

from matplotlib import pyplot as plt

import sys
import rospy
from pack.srv import *

def getintermediatecoordinates(x, y, vx, vy):
    rospy.wait_for_service('service')
    try:
        intermediatecoordinates = rospy.ServiceProxy('service', service1)
        resp1 = intermediatecoordinates(x, y, vx, vy)
        return resp1.xi,resp1.yi
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y vx vy]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 5:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        vx = int(sys.argv[3])
        vy = int(sys.argv[4])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s %s %s %s"%(x, y, vx, vy))
    print((x, y, getintermediatecoordinates(x, y, vx, vy)[0])[2])
    print((x, y, getintermediatecoordinates(x, y, vx, vy)[1])[2])

    p=(x, y, getintermediatecoordinates(x, y, vx, vy)[0])[2]
    q=(x, y, getintermediatecoordinates(x, y, vx, vy)[1])[2]

    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    x = [p]
    y = [q]
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.grid()
    plt.plot(x, y, marker="o", markersize=2, markeredgecolor="red", markerfacecolor="green")
    plt.show()