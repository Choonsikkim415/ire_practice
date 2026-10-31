#!/usr/bin/env python3
"""사각형 경로 순찰 로봇 turtlesim."""


import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_srvs.srv import SetBool


class srv_driver1(Node):
    def __init__(self):
        super().__init__('srv_driver1')
        self.declare_parameter('speed', 1.0)      # 선속도 [m/s]
        self.declare_parameter('turn', 1.0)       # 각속도 [rad/s]
        self.declare_parameter('forward_duration', 1.5)    # 직진시간 [s]
        self.running = False
        self.phase = 'forward'
        self.phase_start = self.get_clock().now()
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.srv = self.create_service(SetBool, 'start_stop', self.on_call)
        self.create_timer(0.02, self.on_timer)

    def on_call(self, req, res):
        if req.data:
            if not self.running:
                self.running = True
                self.phase = 'forward'
                self.phase_start = self.get_clock().now()
        else:
            self.running = False
            self.publish_stop()

        res.success = True
        res.message = 'running' if req.data else 'stopped'
        self.get_logger().info(res.message)
        return res                                 # 짧고 즉시 return!

    def publish_stop(self):
        msg = Twist()
        self.pub.publish(msg)

    def on_timer(self):
        if not self.running:
            return
        now = self.get_clock().now()
        elapsed = (now - self.phase_start).nanoseconds / 1e9

        speed = self.get_parameter('speed').value
        turn = self.get_parameter('turn').value
        forward_duration = self.get_parameter('forward_duration').value

        if forward_duration <= 0 or abs(turn) < 1e-6:
            self.get_logger().error('speed 또는 turn 설정을 확인하세요.')
            self.running = False
            self.publish_stop()
            return

        turn_duration = math.pi / (2.0 * abs(turn))

        if self.phase == 'forward':
            if elapsed >= forward_duration:
                self.phase = 'turn'
                self.phase_start = now

        elif self.phase == 'turn':
            if elapsed >= turn_duration:
                self.phase = 'forward'
                self.phase_start = now

        msg = Twist()

        if self.phase == 'forward':
            msg.linear.x = speed
        elif self.phase == 'turn':
            msg.angular.z = turn

        self.pub.publish(msg)

def main():
    rclpy.init()
    node = srv_driver1()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.publish_stop()
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
