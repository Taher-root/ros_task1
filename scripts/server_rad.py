#!/usr/bin/env python

from __future__ import print_function

from pack.srv import compute_ang_vel,compute_ang_velResponse

import rospy

linear_velocity=0.1

def handle_req(req):
    #global linear_velocity
    print("Returning [%s/%s]"%(linear_velocity,req.radius))
    resp2=compute_ang_velResponse()
    resp2.angular_velocity=linear_velocity//req.radius
    return resp2.angular_velocity

def calc_plot():
    rospy.init_node('service_ang_vel_node')
    s = rospy.Service('serviceangvel', compute_ang_vel, handle_req)
    print("Ready to give angular velocity")
    rospy.spin()

if __name__ == "__main__":
    calc_plot()