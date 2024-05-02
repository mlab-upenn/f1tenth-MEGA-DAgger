# f1tenth-MEGA-DAgger

 This is the repository of MEGA-DAgger for F1TENTH autonomous racing platform.

**mega_dagger_agent** is a ROS2 foxy package.
Move the package in the /src folder of your workspace.
Under the workspace directory, source the overlay and underlay, and colcon build it.
Then, enter the following commandlines for different usage.

**mega_dagger_opponent** contains 2 ROS2 foxy workspaces.
f1tenth_ws includes the pure pursuit package.
is-workspace includes the integration service code to enable the communication between different ROS domain IDs.
Please check [IS official docs](https://integration-service.docs.eprosima.com/en/latest/examples/same_protocol/ros2_change_domain.html) for further details.

## 1 f1tenth_gym_ros Simulation

Run following commands on your PC.

```bash
# modify the path, lidarscan_topic, etc. for your specific usage
# change as "num_agent: 2" in "f1tenth_gym_ros/config/sim.yaml"
# in the 1st terminal
ros2 launch f1tenth_gym_ros gym_bridge_launch.py  # run the simulator
# in the 2nd terminal
conda activate f110_mega-dagger  # enable your specific env to run pytorch, etc.
ros2 run mega_dagger_agent agent_node.py  # self.is_real = False, modify self.lidarscan_topic
# in the 3rd terminal
ros2 run mega_dagger_agent fake_scan_node.py  # run this if you want the modified lidar scan
# in the 4th terminal
ros2 run mega_dagger_agent oppo_node.py  # is_real == False, to enable the opponent car in sim
# in the 5th terminal, if you need to reset initial pose of the ego car
ros2 topic pub /initialpose geometry_msgs/PoseWithCovarianceStamped '{header: {stamp: {sec: 0, nanosec: 0}, frame_id: "map"}, pose: {pose: {position: {x: 1.5, y: 4.5, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: 0.86602540378, w: 0.5}}, covariance: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}}'

```

## 2 Real World Implementation

1 - Run following commands on your PC.

```bash
# connect the same network with the same ROS_DOMAIN_ID as your agent car. 
# modify the path, lidarscan_topic, etc. for your specific usage
# in the 1st terminal
conda activate f110_mega-dagger  # enable your specific env to run pytorch, etc.
ros2 run mega_dagger_agent agent_node.py  # self.is_real = True
# in the 2nd terminal
ros2 run mega_dagger_agent fake_scan_node.py  # run this if you want the modified lidar scan
# in the 3rd terminal
rviz2  # for visualization
```

2 - Run following commands on your agent car.

```bash
# connect the same network with the same ROS_DOMAIN_ID as your PC. 
# in the 1st terminal
ros2 launch f1tenth_system bringup_launch.py  # enable remote control
# in the 2nd terminal
ros2 launch particle_filter localize_launch.py  # enable localization
# in the 3rd terminal
rviz2  # for visualization
```

Enable remote desktop tools like NoMachine if you need.

3 - Run following commands on your opponent car.

```bash
# in f1tenth workspace, running pure pursuit
cd f1tenth_ws/
# in the 1st terminal
ros2 launch f1tenth_stack bringup_launch.py # enable the controller
# in the 2nd terminal
ros2 launch particle_filter localize_launch.py # enable the particle filter to do localization
# in the 3rd terminal
ros2 run pure_pursuit pure_pursuit.py # run pure pursuit to follow the waypoints

# if you enable the agent car's fake scan feature to detect the opponent car, please do the following
# in integration service workspace, enable integration service and ROS2 topic conversion
cd ../is-workspace/
integration-service src/Integration-Service/examples/basic/ros2__domain_id_change.yaml # run the integration service to connect different ros2 topics under different ros2 domain ID
```

Check lidar scan of the agent car to see if the opponent car is detected.

## 3 Performance

Please check the following youtube videos for further details.

[MEGA-DAgger ROS Simulation](https://youtu.be/qApr0d056ck)

[MEGA-DAgger Single Car Experiment - 0317](https://youtu.be/WKTLcDU4JrU)

[MEGA-DAgger Real World Experiment - 0317](https://youtu.be/dhB0yfGq3-U)

[MEGA-DAgger Real World Experiment 2x Speed - 0317](https://youtu.be/mScCIROcDVE)

[MEGA-DAgger Real World Experiment - 0312](https://youtu.be/iLBIYTLuNkQ)

For rosbags, screenshots, screencasts, and videos, please check our [google drive folder](https://drive.google.com/drive/folders/1F-9hQEbKbUTK9yWpuRIfvNrADnqi8esk?usp=drive_link) for more info.
