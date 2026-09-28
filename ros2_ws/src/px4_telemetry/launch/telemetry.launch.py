from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='px4_telemetry',
            executable='telemetry_node',
            name='px4_telemetry',
            output='screen',
            parameters=[{'display_rate': 1.0}],
        )
    ])
