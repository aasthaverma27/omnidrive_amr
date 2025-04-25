<br />
<div align="center">
  <a href="https://github.com/atom-robotics-lab/assets/blob/main/logo_1.png?raw=true">
    <img src="https://github.com/atom-robotics-lab/assets/blob/main/logo_1.png?raw=true" alt="Logo" width="120" height="120">
  </a>
 <h3 align="center">Omnidrive AMR</h3>

  <p align="center">
    This is the repo for the <a href="https://github.com/atom-robotics-lab/omnidrive-amr">Omnidrive-AMR</a> Project, Omnidrive-amr is an autonomous omnidirectional robot made by A.T.O.M Robotics having an 8-axis drive system and capable of autonomous Navigation using various srcipts.
  </p>
</div>
<br />


## About the Project
This project aims to develop a comprehensive ROS2 simulation package tailored for a Omnidrive-amr.This repository shows how to autonomously navigate an omnidirectional robot
### Built With
* [![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://ubuntu.com/)
* [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
* [![ROS 2](https://img.shields.io/badge/ros-%230A0FF9.svg?style=for-the-badge&logo=ros&logoColor=white)](https://www.sphinx-docs.org)

 ## Getting started
Follow these instructions to set up this project on your system.

### Prerequisites

* ROS Humble
Refer to the official [ROS 2 installation guide](https://docs.ros.org/en/humble/Installation.html)
* Gazebo classic
  ```bash
  sudo apt install ros-humble-gazebo-ros-pkgs
  ```
* Robot_localization and Nav2 packages
  ```bash
  source /opt/ros/humble/setup.bash
  sudo apt install ros-humble-robot-localization
  sudo apt install ros-humble-navigation2
  sudo apt install ros-humble-nav2-bringup
  ```

### Installation
 
 1. Make a new workspace
    ```bash
    mkdir -p omnidrive_ws/src
    ```

2. Clone the GPS_Nav repository

    Now go ahead and clone this repository inside the "src" folder of the workspace you just created.

      ```bash
      cd omnidrive_ws/src
      git clone git@github.com:atom-robotics-lab/omnidrive-amr.git
      ```

3. Compile the package

    Follow this execution to compile your ROS 2 package
  
      ```bash
      colcon build --symlink-install
      ```

4. Source your workspace
      ```bash
      source install/local_setup.bash
      ```

## Usage
Our package consists of three directories as follows:-

- The `bot_description` dir contains all the bot model description files.
- The `omni_gz` dir contains all the world description files.
- The `omni_nav` dir contains all the config files for enabling navigation and planning.

### 1. Launch gazebo
* Spawns our robot in a custom gazebo world along with all the necessary plugins.
  ```bash
  ros2 launch omni_gz gazebo.launch.py
  ```

### 2. Navigation
* Launch the navigation file
  ```bash
  ros2 launch omni_nav combined_nav_launch.py
  ```
**_NOTE:_** Make sure that you have installed the navigation dependencies before running the navigation launch file.<br />

[omnidrive-ezgif.com-video-speed.webm](https://github.com/user-attachments/assets/d66f4f6b-5215-47ef-8581-eb2a2ddb6003)

## Contributing

We wholeheartedly welcome contributions!  
They are the driving force that makes the open-source community an extraordinary space for learning, inspiration, and creativity. Your contributions, no matter how big or small, are **genuinely valued** and **highly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/New-Feature`)
3. Commit your Changes (`git commit -m 'Add some New-Feature'`)
4. Push to the Branch (`git push origin feature/New-Feature`)
5. Open a Pull Request

Please adhere to this project's `code of conduct`.

## License

[APACHE 2.0](https://choosealicense.com/licenses/apache-2.0/)

## Contact Us

If you have any feedback, please reach out to us at:  
Our Socials - [Linktree](https://linktr.ee/atomlabs)

## Acknowledgments

* [Our wiki](https://atom-robotics-lab.github.io/wiki)
* [ROS Official Documentation](http://wiki.ros.org/Documentation)
* [Gazebo Tutorials](https://gazebosim.org/docs/latest/tutorials/)
* [Ubuntu Installation guide](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)
* [Nav2 official documentation](https://docs.nav2.org/index.html)
