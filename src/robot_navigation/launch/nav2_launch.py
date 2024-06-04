from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import FindPackageShare

def generate_launch_description():
    # Locate the package and parameter files
    nav2_bringup_dir = FindPackageShare(package='nav2_bringup').find('nav2_bringup')
    nav2_params_file = '/src/robot_navigation/config/nav2_params.yaml'

    return LaunchDescription([
        # Include the Nav2 bringup launch file
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([nav2_bringup_dir, '/launch/navigation_launch.py']),
            launch_arguments={'params_file': nav2_params_file}.items(),
        ),
    ])
