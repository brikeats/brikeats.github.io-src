Title: Ultrasonic sensors in rviz
Date: 2017-10-23
Category: Robots
Tags: robotics, ROS, ultrasonic
Slug: rviz
Author: Brian Keating
Summary: Taking ultrasonic measurements with a raspberry pi + arduino and visualizing them in realtime with ROS/Rviz.


## Ultrasonic Sensors on the Arduino

The primary sensor on my robot will be a [kinect](https://en.wikipedia.org/wiki/Kinect). Playing around with the kinect on my laptop, it's apparent that the depth sensor doesn't work below ~20 cm. It was designed to track people standing a few meters away, and the depth image is black for pixels containing very nearby object(s). 

In order to prevent the robot from smashing into things that are nearby, I plan on using an array of ultrasonic sensors as a "virtual bumper", so that while I'm debugging and developing control/navigation, the robot doesn't destroy itself by crashing into everything. There are currently 4 sensors hotglued to the robot base: 1 forward-facing, 1 backward-facing, and 1 each to the forward-left and forward-right (about 30 degrees off-center).

The sensors require a microcontroller to use. It's possible to use the pins on the pi to drive and read from the sensors. However, 1) the input pins on the pi take 3.3V input, which means you have to step down from 5V, which is a pain for multiple channels; and 2) interrupts from the OS could make it unreliable. When timing the speed of a ping down to the microsecond, the pi may be busy with more heavy-duty computer vision computation, and low latency ultrasonic readings are safety-critical for the robot, so I'm dedicating an arduino to it. The firmware for driving a set of sensors with the arduino uno [is here](https://github.com/brikeats/ROS/blob/master/workspace/src/ultrasonic_array/firmware/ultrasonic_array/ultrasonic_array.ino). There is an [associated ROS node](https://github.com/brikeats/ROS/blob/master/workspace/src/ultrasonic_array/nodes/ultrasonic_array), `ultrasonc_array`, that reads from the serial port, parses the lines, and broacasts the readings as [ROS Range messages](http://docs.ros.org/api/sensor_msgs/html/msg/Range.html). This node also defines the transform (`tf`) of each of the pins; in this way an identity ("front_right_sensor", "rear_center_sensor", etc.) is assigned to the pin numbers that are read from the serial port.

Note that even after the primary echo is detected by the sensor and printed on the serial port by the Arduino, there may still be reverberations and echos from the ping. You need to wait 150-200ms after a reading before sending the next ping so that there's no interference from the previous ping.


## Robot Description in URDF

The frames assigned by `ultrasonic_array` are just strings. In order to define the geometry, I created a package for describing the robot's geometry and wrote [a URDF description of the robot](https://github.com/brikeats/ROS/blob/master/workspace/src/adam_description/urdf/adam.urdf) by following the [ROS tutorial](http://wiki.ros.org/urdf/Tutorials). A few of the components were too complicated to draw manually, so I specified them as 3D models created in Sketchup. There's no Sketchup for Ubuntu (my laptop OS), but it runs fine  with [PlayOnLinux](https://www.playonlinux.com/en/). From Sketchup, export the [3D models as `.dae` files](https://github.com/brikeats/ROS/tree/master/workspace/src/adam_description/meshes), which can be included in the URDF. 

While working on the URDF, you can view the model with rviz with the command `roslaunch adam_description display.launch`. [The launch file](https://github.com/brikeats/ROS/blob/master/workspace/src/adam_description/launch/display.launch) uses [joint_state_publisher](http://wiki.ros.org/joint_state_publisher) and [robot_state_publisher](http://wiki.ros.org/robot_state_publisher) to publish the poses of all the robot components (including the sensors), and launches rviz to view it. My half-finished model looks like this:

![Alt Text]({filename}/images/rviz_screenshot.png)

The actual robot has tank treads and is more complete than the model:

![Alt Text]({filename}/images/robot.jpg)


## Real-time rendering of Range measurements

Putting it all together, define the robot in URDF, broadcast the robot geometry and view it with `roslaunch adam_description display.launch`. Then start the ultrasonic array node with `rosrun ultrasonic_array ultrasonic_array` to begin reading the arduino printouts and broadcasting the Range messages. From in the Rviz GUI, manually add the Range measurements. In order for the Range messages to display correctly, the frame defined in the `ultrasonic_array` must match one of the frames in the URDF description. The result:

# 
<iframe width="560" height="315" src="https://www.youtube.com/embed/xQT_J7t7Gr0?rel=0" frameborder="0" allowfullscreen></iframe>
# 

The Range measurements are displayed as cones which indicate the field of view of the sensor. There's a half second lag, partly due to the wifi -- the visualization node runs on my laptop, but the other nodes are running on the raspberry pi.
