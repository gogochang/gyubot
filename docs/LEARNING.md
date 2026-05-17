# ROS2 자율주행 프로젝트 학습 기록

## Phase 1.5: Custom 로봇 패키지 구축 (From Scratch)

### Step 1: 워크스페이스 및 패키지 생성 (2026-05-17)
- **수행 내용**: `~/gyubot_ws/src` 구조를 만들고 `ros2 pkg create`를 사용하여 `gyubot_description` 패키지를 `ament_cmake` 타입으로 생성함.
- **학습 포인트**: 
    - **Workspace & src 폴더**: ROS2에서 모든 사용자의 소스 코드는 워크스페이스 내부의 `src` 폴더에 위치해야 함.
    - **ament_cmake**: C++ 기반 ROS2 패키지의 표준 빌드 시스템. 이 옵션으로 패키지를 만들면 `CMakeLists.txt`와 `package.xml`이 기본적으로 생성됨.
    - **Description 패키지**: 로봇의 3D 외형 정보(URDF), 물리 엔진용 충돌 메쉬 등 로봇 자체를 정의하는 데이터들을 모아두는 곳.