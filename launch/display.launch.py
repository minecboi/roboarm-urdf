import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    # --- REPLACE WITH YOUR PACKAGE AND URDF NAME ---
    pkg_name = 'roboarm'
    urdf_name = 'roboarm.urdf'
    # -----------------------------------------------

    # Path to the URDF file
    urdf_file = os.path.join(get_package_share_directory(pkg_name), 'urdf', urdf_name)
    
    # Optional: Path to an RViz config file (if you save one later)
    # rviz_config = os.path.join(get_package_share_directory(pkg_name), 'config', 'display.rviz')

    # Read the URDF file using xacro (works for raw URDFs too)
    robot_description = ParameterValue(Command(['xacro ', urdf_file]), value_type=str)

    # 1. Robot State Publisher
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description}]
    )

    # 2. Joint State Publisher GUI (creates the slider window)
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui'
    )

    # 3. RViz2
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        # arguments=['-d', rviz_config] # Uncomment this once you save an RViz config
    )

    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz_node
    ])
