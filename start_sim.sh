#!/bin/bash
set -e

source /opt/ros/humble/setup.bash
source /root/ur_ws_sim/install/setup.bash

# important: do NOT run ros2 launch in background
exec ros2 launch my_ur10e_scene_description scene.launch.py launch_rviz:=true
