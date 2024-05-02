from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    talker_node = Node(
        package='lab1_pkg',
        executable='talker.py',
        name='talker',
        output='screen',
        parameters=[{'v': 1.0}, {'d': 2.0}]
    )

    relay_node = Node(
        package='lab1_pkg',
        executable='relay.py',
        name='relay',
        output='screen'
    )

    return LaunchDescription([
        talker_node,
        relay_node
    ])
