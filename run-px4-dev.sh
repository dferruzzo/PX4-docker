#!/usr/bin/env bash

# Enable X11 access for Docker container
xhost +local:docker

# Run PX4 development container and open Bash
docker run -it --privileged \
    --rm \
    --env LOCAL_USER_ID="$(id -u)" \
    -v "$HOME/src/PX4-Autopilot:/src/PX4-Autopilot:rw" \
    -v /tmp/.X11-unix:/tmp/.X11-unix:ro \
    -e DISPLAY="${DISPLAY:-:0}" \
    --network host \
    --name px4-sitl-gazebo \
    px4io/px4-sitl-gazebo:latest

