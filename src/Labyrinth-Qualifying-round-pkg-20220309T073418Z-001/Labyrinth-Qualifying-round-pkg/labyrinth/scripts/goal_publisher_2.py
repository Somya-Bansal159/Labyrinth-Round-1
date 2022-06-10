#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String, Time, UInt32, Float64, Header
from geometry_msgs.msg import PoseStamped

def talker():
    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)
    rospy.init_node('goal_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    i=0
    while not rospy.is_shutdown():
        i+=1
	goal = PoseStamped()

        goal.header.seq = 0
        goal.header.stamp.secs = rospy.Time.now().secs
        goal.header.stamp.nsecs = rospy.Time.now().nsecs
        goal.header.frame_id = "map"
   
        goal.pose.position.x = 4.352
        goal.pose.position.y = 6.547
        goal.pose.position.z = 0.0

        goal.pose.orientation.x = 0.0
        goal.pose.orientation.y = 0.0
        goal.pose.orientation.z = 0.999
        goal.pose.orientation.w = -0.034

        rospy.loginfo(goal)
        pub.publish(goal)
        rate.sleep()
        if i==5:
        	break
	


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
