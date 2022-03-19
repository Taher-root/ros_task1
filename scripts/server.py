#!/usr/bin/env python

from __future__ import print_function

from pack.srv import service1,service1Response

import rospy

def handle_req(req):
    print("Returning [%s*%s , %s*%s ]"%(req.x, req.vx, req.y, req.vy))
    resp1=service1Response()
    resp1.xi=req.x*req.vx
    resp1.yi=req.y*req.vy
    return resp1

def calc_plot():
    rospy.init_node('service_node')
    s = rospy.Service('service', service1, handle_req)
    print("Ready to give intermediate co-ordinates")
    rospy.spin()

if __name__ == "__main__":
    calc_plot()