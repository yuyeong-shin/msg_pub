#! /usr/bin/env python

import rospy
from can_msgs.msg import Frame

def can_frame_callback(msg):
  received_id = msg.id
  received_data = msg.data[:8]

  print("ID: ", received_id)
  print("Data: ", received_data)

def listener():
    rospy.init_node('listen_can', anonymous=True)
    rospy.Subscriber('/can_tx', Frame, can_frame_callback)    
    rospy.spin()

if __name__ == '__main__':
 # rospy.init_node('two_nodes', anonymous=True)
  try:    
    listener()
  except rospy.ROSInterruptException:
    pass
