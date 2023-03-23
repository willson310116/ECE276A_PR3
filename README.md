# ECE-276A-Project3
## Visual-Inertial SLAM
This is the project 3 of the course UCSD ECE276A: Sensing & Estimation in Robotics.

Implement visual-inertial simultaneous localization and mapping (SLAM) using an extended Kalman filter (EKF).

## Usage:
### Install package:
    pip3 install -r requirement.txt
### Run code:
    python3 main.py -d [dataset] --r [reduce factor for visual features] --w [w noise scale] --v [v noise scale]
### Example:
    python3 main.py --d 03 --r 4 --w 10e-6 --v 100
    python3 main.py --d 10 --r 4 --w 10e-6 --v 100


### Source code description:
- **code/main.py**: Main function.
- **code/mapping.py**: Functions for landmark mapping.
- **code/motion.py**: Functions for motion model.
- **code/observation.py**: Functions for observation model.
- **code/pr3_utils.py**: Functions provided for some transformation.
- **code/slam.ipynb**: For testing the process.
- **code/utils.py**: Functions for transformation and others.
- **code/visual_slam.py**: Functions for visual inertial slam.
- **code/visualization.py**: Functions for visualizing the trajectory and landmark mapping.
    