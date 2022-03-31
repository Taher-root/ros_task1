#!/usr/bin/env python

from __future__ import print_function

from pack.srv import service1,service1Response

import rospy



def handle_req(req):
    t=0
    xint=[]
    yint=[]
    while(t<10):
        print("Returning [%s+%s*%s , %s+%s*%s ]"%(req.x, req.vx, t, req.y, req.vy,t))
        resp1=service1Response()
        #print(resp1.xi)
        (xint).append(req.x+req.vx*t)
        (yint).append(req.y+req.vy*t)
        t=t+1
    resp1.xi=xint
    print(resp1.xi)
    resp1.yi=yint
    print(resp1.yi)
    return resp1.xi,resp1.yi

def calc_plot():
    rospy.init_node('service_node')
    s = rospy.Service('service', service1, handle_req)
    print("Ready to give intermediate co-ordinates")
    rospy.spin()

if __name__ == "__main__":
    calc_plot()