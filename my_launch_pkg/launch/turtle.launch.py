from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(package='turtlesim',
             executable='turtlesim_node'),
        Node(package='my_launch_pkg',
             executable='srv_driver1',
             parameters=[{'speed': 1.0, 'turn': 1.0, 'forward_duration': 1.5,}]),
    ])
