FROM px4io/px4-sitl-ros2:latest

RUN printf '\n\
source /opt/ros/jazzy/setup.bash\n\
source /opt/px4_ros2/install/setup.bash\n\
export ROS_DOMAIN_ID=0\n' >> /root/.bashrc

