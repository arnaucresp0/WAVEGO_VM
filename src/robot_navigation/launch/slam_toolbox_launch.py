# slam_toolbox_launch.py
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='slam_toolbox',
            executable='online_async_launch',
            name='slam_toolbox',
            output='screen',
            parameters=[
                {'params_file': '/src/robot_navigation/config/mapper_params_online_async.yaml'},
                {'use_sim_time': False},  # Set to True if using Gazebo simulation
            ]
        ),
    ])
