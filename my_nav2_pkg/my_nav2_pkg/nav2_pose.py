#!/usr/bin/env python3
"""코드로 Nav2에 목표를 보냄 (RViz 클릭의 코드 버전)"""

import rclpy
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult


def make_pose(nav, x, y, yaw_w=1.0):
    p = PoseStamped()
    p.header.frame_id = 'map'
    p.header.stamp = nav.get_clock().now().to_msg()
    p.pose.position.x = x
    p.pose.position.y = y
    p.pose.orientation.w = yaw_w
    return p


def main():
    rclpy.init()
    nav = BasicNavigator()
    nav.waitUntilNav2Active()                      # AMCL·planner 준비 대기

    # 첫 번째 목적지
    goal = make_pose(nav, 3.0, -2.0)
    nav.goToPose(goal)

    while not nav.isTaskComplete():
        fb = nav.getFeedback()
        if fb:
            print(f'남은 거리: {fb.distance_remaining:.2f} m')

    result = nav.getResult()
    print('결과:', 'SUCCEEDED' if result == TaskResult.SUCCEEDED else result)

    # 두 번째 목적지
    goal = make_pose(nav, 4.15, -2.0)
    nav.goToPose(goal)
    
    while not nav.isTaskComplete():
        fb = nav.getFeedback()
        if fb:
            print(f'남은 거리: {fb.distance_remaining:.2f} m')
    
    result = nav.getResult()
    print('결과:', 'SUCCEEDED' if result == TaskResult.SUCCEEDED else result)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
