#!/usr/bin/env python

import roslib
import rospy
from std_msgs.msg import Float32, Int32
import actionlib
import simulation_control.msg
from sensor_msgs.msg import Range, LaserScan
import random
import tf2_msgs.msg
import geometry_msgs.msg
# Simulate object detection: rostopic pub /Left_sensor std_msgs/Float32 15

class fakeLaserScan:

    def __init__(self):
        # Initialize variables and Take off
        rospy.init_node('publish_test_data')

        # sonarOrientation = rospy.Subscriber('/tf', Tran)

        dataLeft = rospy.Publisher('/L_sensor', Range, queue_size=10)
        dataRight = rospy.Publisher('/R_sensor', Range, queue_size=10)
        dataFront = rospy.Publisher('/F_sensor', Range, queue_size=10)

        scan_pub = rospy.Publisher('/fakeScan', LaserScan, queue_size=10)

        self.sonarReadLeft = 20.0
        self.sonarReadRight = 20.0
        self.sonarReadFront = 20.0

        rospy.Subscriber('/Left_sensor', Float32, self.setLeftSonarValue)
        rospy.Subscriber('/Right_sensor', Float32, self.setRightSonarValue)
        rospy.Subscriber('/Front_sensor', Float32, self.setFrontSonarValue)

        self.pub_tf = rospy.Publisher("/tf", tf2_msgs.msg.TFMessage, queue_size=1)
        while not rospy.is_shutdown():
            count = 0
            # HRLV-MaxSonar-EZ MB1043 reports anything below 30 cm as 30 cm
            # inaccurate readings closer than 50 cm
            t = geometry_msgs.msg.TransformStamped()
            t.header.frame_id = "base_frame"
            t.header.stamp = rospy.Time.now()
            t.child_frame_id = "sonar_left"
            t.transform.translation.x = 0.0
            t.transform.translation.y = 0.0
            t.transform.translation.z = 0.0
            t.transform.rotation.x = 0.0
            t.transform.rotation.y = 0.0
            t.transform.rotation.z = 0.0
            t.transform.rotation.w = 1.0


            leftSonar = Range()
            leftSonar.header.stamp = rospy.Time.now()
            leftSonar.header.frame_id = "sonar_left"
            leftSonar.radiation_type = Range.ULTRASOUND
            leftSonar.min_range = 20.0
            leftSonar.max_range = 500.0
            leftSonar.field_of_view = 0.4
            leftSonar.range = self.sonarReadLeft  #This value should be the readings from the actual sonars
            # print("publish data...  ")
            tfm = tf2_msgs.msg.TFMessage([t])

            self.pub_tf.publish(tfm)
            dataLeft.publish(leftSonar)

            t.header.stamp = rospy.Time.now()
            t.child_frame_id = "sonar_right"
            t.transform.translation.x = 0.0
            t.transform.translation.y = 0.0
            t.transform.translation.z = 0.0
            t.transform.rotation.x = 0.0
            t.transform.rotation.y = 0.0
            t.transform.rotation.z = 1.0
            t.transform.rotation.w = 0.0

            tfm = tf2_msgs.msg.TFMessage([t])

            self.pub_tf.publish(tfm)

            leftSonar.range = self.sonarReadRight
            leftSonar.header.frame_id = "sonar_right"
            dataRight.publish(leftSonar)

            t.header.stamp = rospy.Time.now()
            t.child_frame_id = "sonar_front"
            t.transform.translation.x = 0.0
            t.transform.translation.y = 0.0
            t.transform.translation.z = 0.0
            t.transform.rotation.x = -0.5
            t.transform.rotation.y = 0.5
            t.transform.rotation.z = -0.5
            t.transform.rotation.w = 0.5

            leftSonar.range = self.sonarReadFront
            leftSonar.header.frame_id = "sonar_front"
            dataFront.publish(leftSonar)

            tfm = tf2_msgs.msg.TFMessage([t])

            self.pub_tf.publish(tfm)


    def setLeftSonarValue(self, data):
        self.sonarReadLeft = data.data

    def setRightSonarValue(self, data):
        self.sonarReadRight = data.data

    def setFrontSonarValue(self, data):
        self.sonarReadFront = data.data

if __name__ == '__main__':
    fakeLaserScan()
