#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CameraViewer(Node):
    def __init__(self):
        super().__init__('camera_viewer')
        # Subkripsi ke topic kamera yang ada
        self.subscription = self.create_subscription(
            Image,
            '/sonobot/camera/image_color',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.br = CvBridge()
        self.get_logger().info('Camera Viewer node has been started. Waiting for images...')

    def listener_callback(self, msg):
        try:
            # Mengkonversi pesan ROS Image ke format OpenCV
            current_frame = self.br.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            
            # Menampilkan image dalam window
            cv2.imshow("Camera View - /sonobot/camera/image_color", current_frame)
            cv2.waitKey(1)
        except Exception as e:
            self.get_logger().error(f'Error processing image: {str(e)}')

def main(args=None):
    rclpy.init(args=args)
    camera_viewer = CameraViewer()
    
    try:
        rclpy.spin(camera_viewer)
    except KeyboardInterrupt:
        pass
    finally:
        # Destroy the node explicitly
        camera_viewer.destroy_node()
        rclpy.shutdown()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
