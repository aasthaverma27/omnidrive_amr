#!/usr/bin/env python3
import rclpy
from vel_pub import Controller
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TTP(Node):
    def init(self):
        super().init('bot_controller')
        
        # self.right_vel = 0.0
        # self.left_vel = 0.0
        self.v1=0.0
        self.v2=0.0
        self.v3=0.0
        self.v4=0.0
        self.max_pwm_val = 255
        self.min_pwm_val = 0.0
        self.circumference = 0.10
        self.motor_rpm = 350.0
        # self.wheel_seperation = 0.45
        self.max_speed = (self.circumference * self.motor_rpm) / 60  
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel_esp32', 10)
        # self.subscription = self.create_subscription(Twist, '/cmd_vel', self.pose_callback, 10)
        self.timer = self.create_timer(0.1, self.timer_callback)

    def get_pwm(self,v1,v2,v3,v4):
        v1speedPWM = max(min((v1 / self.max_speed) * self.max_pwm_val, self.max_pwm_val), self.min_pwm_val)
        v2speedPWM = max(min((v2 / self.max_speed) * self.max_pwm_val, self.max_pwm_val), self.min_pwm_val)
        v3speedPWM = max(min((v3 / self.max_speed) * self.max_pwm_val, self.max_pwm_val), self.min_pwm_val)
        v4speedPWM = max(min((v4 / self.max_speed) * self.max_pwm_val, self.max_pwm_val), self.min_pwm_val)
        return v1speedPWM, v2speedPWM, v3speedPWM, v4speedPWM

    def pose_callback(self, msg):
        linear_vel1 = msg.linear.x
        linear_vel2 = msg.linear.y
        linear_vel3 = msg.linear.z
        linear_vel4 = msg.angular.x

        # self.right_vel = linear_vel + (angular_vel * self.wheel_seperation) / 2
        # self.left_vel = linear_vel - (angular_vel * self.wheel_seperation) / 2

        x, y,z,w = self.get_pwm(linear_vel1, linear_vel2, linear_vel3, linear_vel4)

        self.vel = Twist()

        self.vel.linear.x = float(x)
        self.vel.linear.y = float(y)
        self.vel.linear.z = float(z)
        self.vel.angular.x = float(w)
        self.publish_velocity(self.vel)

    def publish_velocity(self, vel):
        self.publisher_.publish(vel)

    def timer_callback(self):
        # No-op placeholder for the timer callback
        pass

def main(args=None):
    rclpy.init(args=args)
    turtle_controller = TTP()

    try:
        rclpy.spin(turtle_controller)
    except KeyboardInterrupt:
        pass
    finally:
        turtle_controller.destroy_node()
        rclpy.shutdown()

if __name__ == 'main':
    main()