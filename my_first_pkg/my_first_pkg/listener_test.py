#!/usr/bin/env python3
"""3주차 강의 예제 — chatter를 받아 출력하는 subscriber."""
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Listener(Node):
    def __init__(self):
        super().__init__('listener_test')
        self.create_subscription(String, 'chatter_test', self.on_msg, 10)

    def on_msg(self, msg):
        self.get_logger().info(f'반갑습니다! : {msg.data}')


def main():
    rclpy.init()
    node = Listener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()


if __name__ == '__main__':
    main()
