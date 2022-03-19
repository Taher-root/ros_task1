#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from std_msgs.msg import String
from pack.srv import *

def check():
    flag=0
    


def listen1(data):
    global radius
    global flag
    radius=int(data.data)
    if(radius==data.data):
        flag=1
    check()
    print(data.data)

def listening():
    rospy.init_node("rad_node")
    rospy.Subscriber("/radius", String, listen1)
    rospy.spin()

def getangvel(radius):
    rospy.wait_for_service('service_ang_vel')
    try:
        angvel = rospy.ServiceProxy('service_ang_vel', compute_ang_vel)
        resp2 = angvel(int(radius))
        return resp2.angular_velocity
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":
    listening()
    print("Hello")
    print((getangvel(radius)))
    



