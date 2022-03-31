#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from pack.srv import *

radius=-1
#rate = rospy.Rate(2)

def move(radius):
    pub = rospy.Publisher('/cmd_vel_mux', Twist, queue_size=1)
    #rospy.init_node('rad_node')
    move = Twist() 
    move.linear.x = 0.1 
    move.angular.z = getangvel(radius)
    while not rospy.is_shutdown(): 
        pub.publish(move)
        #rate.sleep()  

def listen1(data):
    global radius
    radius=int(data.data)
    print(data.data)
    getangvel(radius)
    move(radius)
    print("Listen1")

def listening1():
    print("listening1")
    #rospy.init_node("rad_node1")
    rospy.Subscriber("/radius", String, listen1)
    #rospy.spin()

def decider(data):
    if(radius==int(data.data) and radius!=-1):
        print("Deciderif")
        rospy.Subscriber("/radius", String, listen1).unregister()
    elif(radius!=int(data.data)):
        print("Deciderelse")
        listening1()

def listening():
    rospy.init_node("rad_node1")
    rospy.Subscriber("/radius", String, decider)
    rospy.spin()
    print("Listening")

def getangvel(radius):
    rospy.wait_for_service('service_ang_vel')
    try:
        angvel = rospy.ServiceProxy('service_ang_vel', compute_ang_vel)
        resp2 = angvel(int(radius))
        print(resp2.angular_velocity)
        return resp2.angular_velocity
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":
    listening()
    print("Hello")
    #print((getangvel(radius)))