#!/usr/bin/env python
## This code is based on the listener.py provided in the beginner_tutorial on ROS. 

# listener.py contains a subscriber and a publisher. It subscribes to a topic and converts the recived data before publishing it to another topic.
# Subscribes to /jansson and publishes to /kthfs

import rospy     
from std_msgs.msg import Int32

Q = 0.15  #constant that recieved data will be divided by.  

def publishToNewTopic(data): #creates a publisher to send data to topic /kthfs
	k = data.data / Q
	pub = rospy.Publisher('kthfs', Int32, queue_size=10)
	pub.publish(k);

def passOnRecievedData(data):
    rospy.loginfo(rospy.get_caller_id() + 'Data recieved: %s. Data published to /kthfs: %s' ,    data.data, data.data/Q)
    publishToNewTopic(data)
    

def listener():
    rospy.init_node('listener') #initalizes the node and gives it a name  # anonymous=True
    data = rospy.Subscriber('jansson', Int32, passOnRecievedData) #receieves data from topic /jansson
    rospy.spin() #keeps python from exiting until the node is cancelled

if __name__ == '__main__':
    listener()
