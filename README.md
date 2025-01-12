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
sudo apt-get install ros-foxy-xacro ros-foxy-joint-state-publisher ros-foxy-gazebo*
