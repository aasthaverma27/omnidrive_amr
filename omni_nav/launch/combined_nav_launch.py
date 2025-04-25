from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os

def generate_launch_description():
    localization_launch = os.path.join(get_package_share_directory('omni_nav'), 'launch', 'localization_launch.py'),

    navigation_launch = os.path.join(get_package_share_directory('omni_nav'), 'launch', 'navigation_launch.py')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(localization_launch)
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(navigation_launch)
        )
    ])