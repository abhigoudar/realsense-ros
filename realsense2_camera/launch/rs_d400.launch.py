# License: Apache 2.0. See LICENSE file in root directory.
# Copyright(c) 2022 Intel Corporation. All Rights Reserved.

"""Launch realsense2_camera node."""
import os
import yaml
from launch import LaunchDescription
import launch_ros.actions
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    launch_description = []
    launch_description.append(
        DeclareLaunchArgument(
            name='param_file',
            default_value=PathJoinSubstitution([FindPackageShare('realsense2_camera'), 'config/rs_d400_config.yaml'])
        )
    )
    launch_description.append(
        launch_ros.actions.Node(
        package='realsense2_camera',
        namespace='d400',
        name='d400',
        executable='realsense2_camera_node',
        parameters=[LaunchConfiguration('param_file')],
        output='screen',
        emulate_tty=True,
        )
    )
    return LaunchDescription(launch_description)