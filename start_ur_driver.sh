#!/usr/bin/env bash
# start_ur_driver.sh
set -e
# Source your ROS + workspace environment (what sros does)
source /opt/ros/humble/setup.bash
source /root/ur_ws_sim/install/setup.bash

#source "/opt/ros/humble/setup.bash" && echo "sourced ROS2"
#source "/root/ws_moveit2/install/setup.bash" && echo "sourced Moveit2"

#source "/root/thws_resources/install/setup.bash" && echo "Thws_resources sourced"
#source "/root/thws_simulation/install/setup.bash" && echo "Thws_simulation sourced"
#source "/root/thws_robot_launch/install/setup.bash" && echo "Thws Robot Launch sourced"

#source "calib_mtc/src/calib_mtc/install/setup.bash" && echo "calib_mtc sourced"

#source ~/.bash_aliases
#source ~/.bashrc # adjust to your real workspace

ros2 launch ur_robot_driver ur_control.launch.py   ur_type:=ur10e   robot_ip:="$1"   use_fake_hardware:=false   launch_rviz:=false   use_scaled_trajectory_controller:=true   initial_joint_controller:=scaled_joint_trajectory_controller
# Launch the UR driver
#ros2 launch ur_robot_driver ur_control.launch.py \
#   ur_type:=ur10e robot_ip:="$1" launch_rviz:=false
