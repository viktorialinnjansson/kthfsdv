#!/usr/bin/env python
## calculates a value from a given algorithm, then publishes it to the topic /jansson at a given #frequency.

import rospy
from std_msgs.msg import Int32

def talker(): #creates a publisher with publishes a value to the topic /jansson
    pub = rospy.Publisher('jansson', Int32, queue_size=10)
    rospy.init_node('talker')
    rate = rospy.Rate(20) # publishes 20 times a second
    k = 1
    N = 4
    print k  #print the published value in the terminal.
    
    while not rospy.is_shutdown(): #while the node is running.
        k = k + N
        pub.publish(k)
	print (str(k) + "is being published to \n/jansson")
        rate.sleep() #makes sure the publishing frequency is stable

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
