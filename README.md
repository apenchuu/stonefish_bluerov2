# AUV / ASV Simulation

Need
Install Stonefish from the link https://github.com/patrykcieslak/stonefish.git, follow the instruction on the link.
ROS2 Humble

Installing the ardusim from the link https://github.com/bvibhav/stonefish_bluerov2, follow the instruction on the link (find the docs for ardupilot better for installation... , im use gemini btw lol)

Starting
Make the ROS2 workspace example ros2_ws/src
Clone this repository in the directory ros2_ws/src

run the command colcon build --event-handlers console_direct+ --cmake-args --symlink-install --packages-select stonefish_bluerov2
then source install/setup.bash
then ros2 launch stonefish_bluerov2 blueboat_sim.py (see the launch directory from stonefish_bluerov2 package from different launch file)

for see the camera the robot use this ros2 run stonefish_bluerov2 view_camera.py
