#!/usr/bin/env python
#import roslib; roslib.load_manifest('Lab4')
import rospy
from datetime import datetime
from std_msgs.msg import String

def callback(name_str):
	rospy.loginfo("{string} {time:%H:%M:%S}".format(string=name_str, time=datetime.now()))
	
def listener():
	rospy.init_node('listener1')
	rospy.Subscriber("chatter", String, callback)
	rospy.spin()
	
if __name__ == '__main__':
	listener()
