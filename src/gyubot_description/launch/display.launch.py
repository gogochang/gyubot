import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    # 1. 패키지 설치 경로 탐색
    # 빌드된 패키지(gyubot_description)의 공유 폴더(share) 위치를 찾습니다.
    pkg_description = get_package_share_directory('gyubot_description')

    # 2. Xacro 파일 절대 경로 설정
    xacro_file = os.path.join(pkg_description, 'urdf', 'gyubot.urdf.xacro')

    # ROS2 Humble 버전의 일부 환경에서는 xacro 명령어의 결과물(XML 문자열)을 단순 문자열이 아닌
    # ParameterValue 타입으로 감싸우저야 하는 경우가 발생함.
    robot_description_content = ParameterValue(
        Command(['xacro ', xacro_file]),
        value_type=str
    )

    # 3. 로봇 상태 게시 (Robot State Publisher) 노드
    # URDF/Xacro 파일을 읽어서 시스템 전역에 로봇의 뼈대 정보를 알려줍니다.
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{
            # xacro 명령어로 파일을 변환한 결과물 robot_description 파라미터로 넘깁니다.
            'robot_description': robot_description_content
        }]
    )

    # 4. 관절 상태 제어 (Joint State Publisher GUI) 노드
    # 로봇의 움직이는 관절(바퀴 등)을 슬라이더로 절할 수 있는 창을 띄웁니다.
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui'
    )

    # 5. 시각화(RViz2) 노드
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
    )

    # 6. 실행할 노드들의 묶음을 반환
    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz_node
    ])
