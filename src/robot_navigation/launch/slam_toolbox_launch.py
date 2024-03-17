# slam_toolbox_launch.py
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='slam_toolbox',
            executable='online_async_slam',
            name='slam_toolbox',
            output='screen',
            parameters=[
                {'use_sim_time': False},  # Set to True if using Gazebo simulation
                # Add any other SLAM Toolbox parameters if needed
            ]
        ),
    ])
