#!/usr/bin/env python

import rospy
from can_msgs.msg import Frame
import std_msgs.msg

def can_frame_callback(msg):
  received_id = msg.id
  received_data = msg.data[:8]

  print("ID: ", received_id)
  print("Data: ", received_data)

def talker():
  pub = rospy.Publisher('/can_rx', Frame, queue_size=10)
  rospy.init_node('talker_can', anonymous=True)
  r = rospy.Rate(10)
  msg = Frame()
  
  while not rospy.is_shutdown():
#    msg.header.seq += 1
    msg.header.stamp = rospy.Time.now()
    msg.header.frame_id = 'ros_to_kvaser'

    msg.id = 33
    msg.is_rtr = 0
    msg.is_extended = 0
    msg.is_error = 0
    msg.dlc = 8

    msg.data = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08]

    pub.publish(msg)
    r.sleep()

def listener():
    rospy.Subscriber('/can_tx', Frame, can_frame_callback)

    rospy.init_node('listen_can', anonymous=True)
    
    print("listener")
    rospy.spin()

if __name__ == '__main__':
 # rospy.init_node('two_nodes', anonymous=True)
  try:
    talker()
    listener()
  except rospy.ROSInterruptException:
    pass
