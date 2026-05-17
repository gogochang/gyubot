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

### Step 2: 로봇 모델링 기초 구성
- **수행 내용**: URDF 모델링을 위한 표준 디렉토리(urdf, meshes, launch, rviz, config) 생성 및 기본 `base_link` xacro 파일 작성.
- **학습 포인트**:
    - **URDF & Xacro**: 로봇을 트리 구조(Tree)로 모델링하는 XML 형식. Xacro를 통해 변수와 매크로를 사용하여 코드를 재사용함.
    - **Base Link**: 로봇을 구성하는 모든 부품이 파생되는 최상위 루트(Root) 좌표계.
