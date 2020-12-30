#!/usr/bin/env python
#import roslib; roslib.load.manifest('Lab4')
import rospy
from std_msgs.msg import String

def talker():
	pub = rospy.Publisher('chatter', String)
	rospy.init_node('talker1')
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		name_str = "Sokolov A.S."
		pub.publish(name_str)
		rate.sleep()
		
if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
