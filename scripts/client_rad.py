#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from pack.srv import *

radius = 5

def listen1(data):
    global radius
    radius = int(data.data)
    print(data.data)
    # rospy.on_shutdown((getangvel(radius)))
    # rospy.Subscriber("/radius", String, listen1).unregister()
    print((getangvel(radius)))
    move(radius)

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
        print("Service call failed: %s" % e)

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
# rate = rospy.Rate(0.5)

def move(radius):
    #rospy.init_node('rad_node')
    move = Twist() 
    move.linear.x = 0.1 
    move.angular.z = getangvel(radius)

# while not rospy.is_shutdown(): 
#     pub.publish(move)
#     rate.sleep() 

if __name__ == "__main__":
    listening()
    #print("Hello")
