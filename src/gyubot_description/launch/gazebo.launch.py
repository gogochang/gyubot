import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    # 1. 패키지 경로 설정
    pkg_description = get_package_share_directory('gyubot_description')
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')

    # 2. Xacro 파일 경로
    xacro_file = os.path.join(pkg_description, 'urdf', 'gyubot.urdf.xacro')

    # robot_description을 ParameterValue로 감싸기
    robot_description_content = ParameterValue(
        Command(['xacro ', xacro_file]),
        value_type=str
    )

    # 3. Robot State Publisher 노드 (URDF 해석)
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{
            'robot_description': robot_description_content,
            'use_sim_time': True # 시뮬레이션 시간을 사용하도록 설정
        }]
    )

    # 4. Gazebo 실행 (기본 월드)
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py')
        )
    )

    # 5. Gazebo에 로봇 스폰(소환)
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=[
            '-topic', 'robot_description', 
            '-entity', 'gyubot',
            '-z', '0.2'
            ],
        output='screen'
    )

    return LaunchDescription([
        robot_state_publisher_node,
        gazebo,
        spawn_entity
    ])