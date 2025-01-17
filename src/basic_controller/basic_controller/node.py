#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class BasicNode(Node):
    
    def __init__(self, nodeName):
        super().__init__(node_name=nodeName)
        self.get_logger().info("ROS2 Node Started")
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("ROS2 Node Log from timer")

def main(args=None):
    rclpy.init(args=args)
    node = BasicNode("first_node")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()