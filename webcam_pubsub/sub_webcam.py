import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class ImageSubscriber(Node):

    def __init__(self):
        super().__init__('Image_subscriber')
        self.subscription = self.create_subscription(Image,'image_raw',self.listener_callback,10)
        self.cv_bridge = CvBridge()
        
    def listener_callback(self, msg):
        image = self.cv_bridge.imgmsg_to_cv2(msg, 'bgr8') 
        cv2.imshow("webcam",image)
        cv2.waitKey(10)
        


def main(args=None):
    rclpy.init(args=args)

    webcam_subscriber = ImageSubscriber()

    rclpy.spin(webcam_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    webcam_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()