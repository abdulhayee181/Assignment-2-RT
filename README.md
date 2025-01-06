# Assignment-2-RT-part2 ROS2
- Turtle Simulation with Robot

## Overview

In this assignment, we replicate the same robot behavior that was previously implemented using the **turtlesim** package, but in ROS2. The robot is already spawned at the position `(2,2)` in the Gazebo simulation, and we need to create a ROS2 package with a single node that will move the robot around in the simulation environment.

## Prerequisites

Before starting, make sure your system is set up with **ROS2 Foxy** and other necessary packages.

### System Requirements:
- ROS2 Foxy
- Gazebo simulation
- Xacro, Joint State Publisher, and other ROS2 dependencies

## Setup Instructions

### 1. Install ROS2 Foxy and Required Packages

Start by updating your system and installing the necessary dependencies:

```bash
sudo apt-get update
sudo apt-get upgrade  # This might take a while
sudo apt-get install ros-foxy-xacro ros-foxy-joint-state-publisher ros-foxy-gazebo
```
### 2. Switch to the ROS2 Branch

After cloning the repository, change to the `robot_urdf` directory and switch to the ROS2 branch:

```bash
cd robot_urdf
git checkout ros2
```
### 3. Install ROS2 Dependencies

Ensure that all the required dependencies are installed. Run the following commands:

```bash
sudo apt-get update
sudo apt-get upgrade  # This might take a while
sudo apt-get install ros-foxy-xacro ros-foxy-joint-state-publisher ros-foxy-gazebo*
```
### 4. Launch Gazebo with ROS2

To launch the simulation environment and spawn the robot at the starting coordinates `(2,2)`, execute the following command:

```bash
ros2 launch gazebo.launch.py
```
### 5. Create a ROS2 Package for Robot Control

Now that the robot model and simulation are set up, you need to create a new ROS2 package to handle the movement of the robot. Use the following command to create a new Python-based ROS2 package:

```bash
ros2 pkg create --build-type ament_python move_turtle
```
