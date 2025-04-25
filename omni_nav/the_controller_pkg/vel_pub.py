import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class Controller(Node):
    def __init__(self):
        super().__init__('wheel_controller')
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscription = self.create_subscription(Twist, '/cmd_vel', self.timer_callback, 10)

        self.timer = self.create_timer(0.1, self.timer_callback)  # 10 Hz

    def inverse_kinematics(self, vel_x, vel_y, theta, dist_wheel, theta_vel):
        # Defining some variables to use in equation
        sqrt_2 = math.sqrt(2) 
        cos_theta = math.cos(theta)
        sin_theta = math.sin(theta)
        v_x = vel_x / sqrt_2
        v_y = vel_y / sqrt_2
        l_Q = dist_wheel * theta_vel

        # Equations of all four wheels
        v_1 = (v_x * (cos_theta + sin_theta)) + (v_y * (sin_theta - cos_theta)) - l_Q
        v_2 = (v_x * (cos_theta - sin_theta)) + (v_y * (sin_theta + cos_theta)) - l_Q
        v_3 = (v_x * (-cos_theta - sin_theta)) + (v_y * (-sin_theta + cos_theta)) - l_Q
        v_4 = (v_x * (-cos_theta + sin_theta)) + (v_y * (-sin_theta - cos_theta)) - l_Q

        return v_1, v_2, v_3, v_4

    def publish_wheel_velocities(self, vel_x, vel_y, theta, dist_wheel, theta_vel):
        v_1, v_2, v_3, v_4 = self.inverse_kinematics(vel_x, vel_y, theta, dist_wheel, theta_vel)

        # twist_msg = Twist()
        # twist_msg.linear.x = v_1
        # twist_msg.linear.y = v_2
        # twist_msg.linear.z = v_3
        # twist_msg.angular.x = v_4

        # Publishing to /cmd_vel topic
        # self.cmd_vel_pub.publish(twist_msg)
        self.get_logger().info(f'initial wheel velocities: {v_1}, {v_2}, {v_3}, {v_4}')

    def timer_callback(self, msg):
        # Example values for testing
        vel_x = msg.linear.x # Linear velocity in x
        vel_y = msg.linear.y  # Linear velocity in y
        theta = math.pi / 4  # 45 degrees in radians
        dist_wheel = 0.25  # Distance of wheel from center of chassis
        theta_vel = 0.1  # Angular velocity

        self.publish_wheel_velocities(vel_x, vel_y, theta, dist_wheel, theta_vel)

def main(args=None):
    rclpy.init(args=args)
    controller = Controller()
    rclpy.spin(controller)
    controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
