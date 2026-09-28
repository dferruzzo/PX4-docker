# PX4 ROS 2 telemetry

Place `px4_telemetry/` under `ros2_ws/src/` on the host. Start PX4 SITL and the MicroXRCEAgent (UDP port 8888), then open a shell in your ROS 2 container:

```bash
docker exec -it px4-ros2 bash
source /opt/ros/$ROS_DISTRO/setup.bash
source /opt/px4_ros2/install/setup.bash
cd /root/ros2_ws
colcon build --symlink-install --packages-select px4_telemetry
source install/setup.bash
ros2 launch px4_telemetry telemetry.launch.py
```

Alternatively: `ros2 run px4_telemetry telemetry_node --ros-args -p display_rate:=2.0`.

The node subscribes with BEST_EFFORT QoS to `/fmu/out/vehicle_attitude`, `/fmu/out/vehicle_local_position`, and `/fmu/out/vehicle_status`. It prints attitude in degrees, local NED position and velocity, and numeric PX4 arming/navigation states. Validity flags are checked for position and velocity. Ensure the installed `px4_msgs` definitions match the PX4 firmware version.
