cmake_minimum_required(VERSION 3.8)
project(gyubot_description)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()

# Install directories
# src/ 폴더에 있는 리소스들(urdf, launch 등)을 설치(install) 폴더의 share 경로로 복사합니다.
# 이 과정을 거쳐야 ros2 launch 명령어가 해당 파일들을 찾을 수 있습니다.
install(
  DIRECTORY urdf meshes launch rviz config
  DESTINATION share/${PROJECT_NAME}
)