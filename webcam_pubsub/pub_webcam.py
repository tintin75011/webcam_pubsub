import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class ImagePublisher(Node):

    def __init__(self):
        super().__init__('Image_publisher')
        self.publisher_ = self.create_publisher(Image, 'image_raw', 10)
        timer_period = 0.01  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.cap = cv2.VideoCapture(0)
        self.cv_bridge = CvBridge()

    def timer_callback(self):
        ret, frame = self.cap.read()

        if ret == True :
            self.publisher_.publish(self.cv_bridge.cv2_to_imgmsg(frame,'bgr8'))
        self.get_logger().info('publishing video frame')


def main(args=None):
    rclpy.init(args=args)

    node = ImagePublisher()

    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()