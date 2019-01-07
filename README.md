# Simulation of Ultrasonic sensor for the F651 Drone
Drone was initialy developed by Students at University Of Halmstad. Their github can be found using this link:
https://github.com/CPS2018

Run On Drone:
$ export ROS_MASTER_URI=http://10.42.0.1:11311
$ export ROS_IP=10.42.0.1 
$ export ROS_HOSTNAME=10.42.0.1
$ roslaunch autonomous_offboard rosserial.launch

Run On Your Compuer:
$ export ROS_MASTER_URI=http://10.42.0.1:11311
$ export ROS_IP=10.42.0.81
$ rosrun beginner_tutorials fakeLaserScan.py

In a new Terminal Run on Your Computer:
$ export ROS_MASTER_URI=http://10.42.0.1:11311
$ export ROS_IP=10.42.0.81
$ rosrun tf static_transform_publisher 0.0 0.0 0.0 0.0 0.0 0.0 /base_frame /sonar_left 1000 &
$ rosrun tf static_transform_publisher 0.0 0.0 0.0 0.0 0.0 0.0 /base_frame /sonar_right 1000 &
$ rosrun tf static_transform_publisher 0.0 0.0 0.0 0.0 0.0 0.0 /base_frame /sonar_front 1000 &
$ rosrun rviz rviz

When rviz opens:
Import configuration file: RVIZ-3RangeBeams.rviz
