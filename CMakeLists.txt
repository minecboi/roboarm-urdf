cmake_minimum_required(VERSION 3.8)
project(roboarm) # REPLACE THIS

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)

# Install directories so ROS 2 can find your files
install(
  DIRECTORY launch meshes urdf config
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
