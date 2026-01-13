#!/usr/bin/env bash

set -e





cd /root/ur_ws_sim
source /opt/ros/humble/setup.bash
source /root/ur_ws_sim/install/setup.bash

source install/hemi_motion_rs/share/hemi_motion_rs/local_setup.bash

                  # source your ROS environment

# Launch MoveIt
ros2 control switch_controllers   --activate scaled_joint_trajectory_controller     --strict   --start-asap
ros2 launch my_ur10e_moveit_config custom_rs.launch.py
