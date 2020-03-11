#start of code snippet from Owen


import rospy  # this is the module required for all simulation communication

# start of wheel control code
from wheel_control.msg import wheelSpeed  # this is a required module for the drive communication

rospy.init_node("controller")

class WheelController:

    def __init__(self):
        self.wheel_pub = rospy.Publisher("/gazebo_wheelControl/wheelSpeedTopic", wheelSpeed, queue_size=1)

    def drive_wheels(self, left, right):
        # type: (float, float) -> None
        # left and right are numbers between -1 and 1
        msg = wheelSpeed()
        msg.left = left
        msg.right = right
        msg.wheelMode = 0
        self.wheel_pub.publish(msg)
        #print(msg)


# end of wheel control code

# start of laser scan code
from sensor_msgs.msg import LaserScan


class LaserListener:

    def __init__(self):
        self.laserSub = rospy.Subscriber("/leddar/leddarData", LaserScan, self.laser_callback, queue_size=1)
        self.laserRanges = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

    def laser_callback(self, msg):
        # type: (LaserScan) -> None
        self.laserRanges = msg.ranges


# end of laser scan code access laserRanges for an array of all measured distances from the laser sensors

# start of localization stuff
from geometry_msgs.msg import Point
from std_msgs.msg import Float32


class LocationHeading:

    def __init__(self):
        self.fixSub = rospy.Subscriber("/fix/metres", Point, self.fix_callback, queue_size=1)
        self.headingSub = rospy.Subscriber("/heading",Float32, self.heading_callback, queue_size=1)
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.heading = 0.0

    def fix_callback(self, msg):
        # type: (Point) -> None
        self.x = msg.x
        self.y = msg.y
        self.z = msg.z

    def heading_callback(self, msg):
        # type: (Float32) -> None
        self.heading = msg.data


# end of localization stuff


#initiallize classes to get and send data to gazebo
locHead  = LocationHeading()
laser = LaserListener()
wheel = WheelController()
#end of initialization

# start of control loop snippet

while not rospy.is_shutdown():  #this will run until gazebo is shut down or CTRL+C is pressed in the ubuntu window that is running this code
    minRange = 99 #initialize minRange to a value larger than what will be recieved
    for x in range(0, 15): #iterate through the ranges list
        if laser.laserRanges[x] < minRange: #if the current range is smaller than the smallest know range
            minRange = laser.laserRanges[x] #update the range
    if minRange < 5: #if there is something closer than 5m in front of the rover
        wheel.drive_wheels(-0.7, 0.7) #turn
    else:
        wheel.drive_wheels(0.5, 0.5) #go staright. Made slow for scanning.
    print("Current Heading: ", locHead.heading, "Current x val: ", locHead.x, "RightMostLaser: ", laser.laserRanges[0]) #print some random data to the command line

# the rover doesn't stop even after the code is stopped. Need to implement that. 
# end of control loop snippet
