#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Imu 


rospy.init_node('move_robot_node')
pub = rospy.Publisher('/cmd_vel', Imu, queue_size=1)
rate = rospy.Rate(2)
move = Twist()
imu = Imu()

move.linear.x = 0.5 #Move the robot with a linear velocity in the x axis
move.angular.z = 0.5 #Move the with an angular velocity in the z axis
imu.orientation_covariance = [0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
imu.orientation.x = 3


while not rospy.is_shutdown(): 
  pub.publish(imu)
  rate.sleep()
