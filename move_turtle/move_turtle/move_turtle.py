import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_srvs.srv import SetBool
from geometry_msgs.msg import Point
from nav_msgs.msg import Odometry

# Global variable to control robot movement
is_moving = True

# Service callback to handle start/stop commands
def handle_stop_restart(request, response):
    global is_moving
    is_moving = request.data
    response.success = True
    response.message = "Robot movement " + ("started" if is_moving else "stopped")
    return response

# Callback to process odometry data
def odom_callback(self, msg):
    x_meters = msg.pose.pose.position.x
    y_meters = msg.pose.pose.position.y

    # Convert to feet
    x_feet = x_meters * 3.28
    y_feet = y_meters * 3.28

    # Publish the position in feet
    position_msg = Point()
    position_msg.x = x_feet
    position_msg.y = y_feet
    self.position_publisher.publish(position_msg)

    self.get_logger().info(f"Published position in feet: x={x_feet:.2f}, y={y_feet:.2f}")

class MoveRobotNode(Node):
    def __init__(self):
        super().__init__('move_turtle_node')

        self.position_publisher = self.create_publisher(Point, 'robot_position_feet', 10)
        self.odom_subscriber = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)

        # Service to stop/restart the robot
        self.stop_restart_service = self.create_service(SetBool, 'stop_restart_robot', handle_stop_restart)
        self.get_logger().info("Stop/Restart service is ready!")

        # Create publisher to send velocity commands
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        # Set up a timer that runs every 1 second
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info("Moving turtle Node has been started!")

    def timer_callback(self):

        global is_moving
        if not is_moving:
            self.get_logger().info("Robot is stopped.")
            return
        msg = Twist()
        # Move forward at a linear speed of 0.5 m/s, no rotation
        msg.linear.x = 0.5
        msg.angular.z = 0.0
        self.publisher.publish(msg)
        self.get_logger().info('Moving robot forward with linear velocity: 0.5 m/s')





def main(args=None):
    rclpy.init(args=args)
    node = MoveRobotNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
