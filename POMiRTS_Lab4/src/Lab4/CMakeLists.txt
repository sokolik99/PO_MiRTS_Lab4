cmake_minimum_required(VERSION 3.0.2)
project(Lab4)

find_package(catkin REQUIRED COMPONENTS
	roscpp
	rospy
	std_msgs
	message_generation
)

generate_messages(
	DEPENDENCIES
	std_msgs
)

catkin_package(
	LIBRARIES Lab4
	CATKIN_DEPENDS message_runtime roscpp rospy
)

catkin_install_python(PROGRAMS
	nodes/Publisher1.py
	nodes/Subscriber1.py
	DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
