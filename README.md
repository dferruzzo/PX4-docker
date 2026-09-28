# How to run it

- Inicie o `QGronudControl` (QGC).

- Num terminal rode o container contendo o PX4.

```bash
./run-px4-dev.sh
```

O QGC deve reconhecer o PX4 de forma automática.

-  Num outro terminal rode o container ROS2:
```bash
./run-px4-ros2.sh
```

Num outro terminal rode:

```bash
docker exed -it px4-ros2 bash
````

Nele você terá o folder `ros_ws` disponível. Rode:

```bash
cd /root/ros2_ws

source /opt/ros/$ROS_DISTRO/setup.bash

colcon build --symlink-install

source install/setup.bash
```

## Compilar e executar o projeto

Para compilar o projeto rode:

```bash
source /opt/ros/$ROS_DISTRO/setup.bash
source /opt/px4_ros2/install/setup.bash

cd /root/ros2_ws

colcon build --symlink-install \
    --packages-select px4_telemetry

source install/setup.bash
``` 

Executar o projeto

```bash
ros2 launch px4_telemetry telemetry.launch.py
```

ou

```bash
ros2 run px4_telemetry telemetry_node \
    --ros-args -p display_rate:=2.0
```

