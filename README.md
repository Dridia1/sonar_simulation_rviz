# Simulation of Ultrasonic sensor for the F651 Drone
Drone was initialy developed by Students at University Of Halmstad. Their github can be found using this link:
https://github.com/CPS2018

# Run On Drone: #
    1. $ export ROS_MASTER_URI=http://10.42.0.1:11311
    2. $ export ROS_IP=10.42.0.1 
    3. $ export ROS_HOSTNAME=10.42.0.1
    4. $ roslaunch autonomous_offboard rosserial.launch


# Run On Your Compuer: # 
    1. $ export ROS_MASTER_URI=http://10.42.0.1:11311
    2. $ export ROS_IP=10.42.0.81
    3. $ rosrun sonar_simulation_rviz sonar_simulation_rviz.py

# In a new Terminal Run on Your Computer: #
    1. $ export ROS_MASTER_URI=http://10.42.0.1:11311
    2. $ export ROS_IP=10.42.0.81
    3. $ rosrun tf static_transform_publisher 0.0 0.0 0.0 0.0 0.0 0.0 /base_frame /sonar_left 1000 &
    4. $ rosrun tf static_transform_publisher 0.0 0.0 0.0 0.0 0.0 0.0 /base_frame /sonar_right 1000 &
    5. $ rosrun tf static_transform_publisher 0.0 0.0 0.0 0.0 0.0 0.0 /base_frame /sonar_front 1000 &
    6. $ rosrun rviz rviz
    7. When rviz opens, import the configuration file: RVIZ-3RangeBeams.rviz
