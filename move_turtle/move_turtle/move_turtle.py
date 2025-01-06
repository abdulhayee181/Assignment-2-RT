import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MoveRobotNode(Node):
    def __init__(self):
        super().__init__('move_turtle_node')
        # Create publisher to send velocity commands
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        # Set up a timer that runs every 1 second
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info("Moving turtle Node has been started!")

    def timer_callback(self):
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
