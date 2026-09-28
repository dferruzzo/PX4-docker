#!/usr/bin/env bash

# Get the directory where this script is located
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

# ROS2 workspace relative to the script directory
ROS2_WS="$SCRIPT_DIR/ros2_ws"

# Run ROS2 container with Micro XRCE-DDS Agent
docker run -it \
    --rm \
    --network host \
    --ipc host \
    -e ROS_DOMAIN_ID=0 \
    -v "$ROS2_WS:/root/ros2_ws:rw" \
    -w /root/ros2_ws \
    --name px4-ros2 \
    my-px4-sitl-ros2:latest \
    MicroXRCEAgent udp4 -p 8888

