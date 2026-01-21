# AUV / ASV Simulation

This repository contains simulation scenarios and configurations for Autonomous Underwater Vehicles (AUV) and Autonomous Surface Vehicles (ASV) using Stonefish and ROS 2.

## Prerequisites

Before running the simulation, ensure you have the following installed:

1.  **ROS 2 Humble**: Make sure a compatible version of ROS 2 is installed on your system.
2.  **Stonefish Simulator**: Install the Stonefish simulator by following the instructions in the official repository:
    *   [https://github.com/patrykcieslak/stonefish.git](https://github.com/patrykcieslak/stonefish.git)

3.  **ArduPilot Simulation**: Set up the ArduPilot simulation environment.
    *   This setup is based on: [https://github.com/bvibhav/stonefish_bluerov2](https://github.com/bvibhav/stonefish_bluerov2)
    *   *Note: It is recommended to follow the official ArduPilot documentation for installing the SITL (Software In The Loop) environment properly. (I assume you use Gemini, by the way lol)*

## Installation

1.  **Create a ROS 2 Workspace** (if you haven't already):
    ```bash
    mkdir -p ~/ros2_ws/src
    cd ~/ros2_ws/src
    ```

2.  **Clone this Repository**:
    Clone this repository into the `src` folder of your workspace:
    ```bash
    git clone <URL_TO_THIS_REPO>
    ```

3.  **Build the Package**:
    Navigate to the root of your workspace and build the package using `colcon`:
    ```bash
    cd ~/ros2_ws
    colcon build --event-handlers console_direct+ --cmake-args --symlink-install --packages-select stonefish_bluerov2
    ```

4.  **Source the Setup Script**:
    Load the ROS 2 environment for the workspace:
    ```bash
    source install/setup.bash
    ```

## Usage

### Running the Simulation

To start the simulation (e.g., for the Blueboat), run the launch file:

```bash
ros2 launch stonefish_bluerov2 blueboat_sim.py
```

*Tip: Check the `launch/` directory in the `stonefish_bluerov2` package to see other available launch files for different vehicle configurations.*

### Viewing the Camera Feed

To view the live video feed from the robot's camera, run the following command in a new terminal (don't forget to source the workspace first):

```bash
ros2 run stonefish_bluerov2 view_camera.py
```
