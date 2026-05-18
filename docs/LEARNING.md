# ROS2 자율주행 프로젝트 학습 기록

## Phase 1.5: Custom 로봇 패키지 구축 (From Scratch)

### Step 1: 워크스페이스 및 패키지 생성 (2026-05-17)
- **수행 내용**: `~/gyubot_ws/src` 구조를 만들고 `ros2 pkg create`를 사용하여 `gyubot_description` 패키지를 `ament_cmake` 타입으로 생성함.
- **실행 명령어**:
    ```
    // 1. 워크스페이스 루트로 이동
    cd ~/gyubot_ws

    // 2. 소스 폴더 생성
    mkdir -p src

    // 3. 패키지 생성 (ROS2 Humble 환경 소싱 필요)
    cd src
    ros2 pkg create --build-type ament_cmake gyubot_description

    ```
- **학습 포인트**: 
    - **Workspace & src 폴더**: ROS2에서 모든 사용자의 소스 코드는 워크스페이스 내부의 `src` 폴더에 위치해야 함.
    - **ament_cmake**: C++ 기반 ROS2 패키지의 표준 빌드 시스템. 이 옵션으로 패키지를 만들면 `CMakeLists.txt`와 `package.xml`이 기본적으로 생성됨.
    - **Description 패키지**: 로봇의 3D 외형 정보(URDF), 물리 엔진용 충돌 메쉬 등 로봇 자체를 정의하는 데이터들을 모아두는 곳.
---
### Step 2: 로봇 모델링 기초 구성 (2026-05-17)
- **수행 내용**: URDF 모델링을 위한 표준 디렉토리(urdf, meshes, launch, rviz, config) 생성 및 기본 `base_link` xacro 파일 작성.
- **학습 포인트**:
    - **URDF & Xacro**: 로봇을 트리 구조(Tree)로 모델링하는 XML 형식. Xacro를 통해 변수와 매크로를 사용하여 코드를 재사용함.
    - **Base Link**: 로봇을 구성하는 모든 부품이 파생되는 최상위 루트(Root) 좌표계.
---
### Step 3: RViz2 시각화 및 Launch 구성 (2026-05-17)
- **수행 내용**: `display.launch.py` 작성 및 `CMakeLists.txt` 리소스 배포 설정.
- **실행 명령어**:
    ```
    colcon build --symlink-install --packages-select gyubot_description
    source install/setup.bash
    ros2 launch gyubot_description display.launch.py
- **학습 포인트**:
    - **Launch System**: 다수의 ROS2 노드를 체계적으로 관리하고 실행하는 Python 스크립트 구조 이해.
    - **CMake Install**: 소스 폴더의 리소스(URDF, Launch 등)를 실행 가능한 `install/` 경로로 배포하는 규칙 설정
- **트러블슈팅 기록**:
    1. **패키지 이름 불일치**: 폴더명(`gyubot_description`)과 파일 내부 이름(`gybot_description`)이 달라 `colcon build`가 인식하지 못하는 문제 해결.
    2. **robot_description 파라미터 파싱 에러**: Xacro의 XML 결과물 `ParameterValue`로 감싸지 않아 발생한 YAML 파싱 오류를 `launch_ros.parameter_description` 사용으로 해결.
---
### Step 4: 로봇 바퀴(Wheels) 및 Joint 설정 (2026-05-18)
- **수행 내용**: gyubot.urdf.xacro 파일을 수정하여 로봇 본체(base_link)에 4개의 바퀴를 부착하고, 회전 가능한 관절(continuous joint)을 설정함.
- **학습 포인트**:
    - **Xacro Property (상수)**: `<xacro:property>`를 사용하여 로봇의 치수 데이터(너비, 길이, 반지름 등)를 변수로 관리, 크기 변경 시 유지보수성을 극대화함.
    - **Xacro Macro (매크로)**: `<xacro:macro>`를 사용하여 반복되는 바퀴 모델링 코드를 함수처럼 정의하고 재사용함
    - **Joint (관절)**: 부모 링크(base_link)와 자식 링크(wheel)를 연결, 바퀴처럼 무한히 회전해야 하는 경우 continuous 타입을 사용하며, `<axis>` 태그로 회전축(y축)을 지정함.
    - **좌표계 변환 (TF)**: `rpy="${pi/2} 0 0"` 설정을 통해 기본적으로 세워져 있는 원통(cylinder) 모델을 90도로 눕혀서 바퀴 형태로 변환함.
- **트러블슈팅 기록**:
    1. **RViz2 재질(material) 파싱 에러**: Visual material must contain a name attribute 에러 발생. ROS2(Humble)의 URDF 파서는 <material> 태그 사용 시 반드시 name 속성을 요구함을 확인하고, <material name="blue"> 형식으로 수정하여 시각화 문제를 해결함.