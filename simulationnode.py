import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton
from PySide6.QtCore import QTimer
import rclpy
from rclpy.node import Node
from std_msgs.msg import String  # Example message type; replace with actual

class Ros2Listener(Node):
    def __init__(self):
        super().__init__('ros2_listener')
        # Subscribe to model info topic; replace with actual message type and topic
        self.subscription = self.create_subscription(
            String,
            '/model/info',
            self.listener_callback,
            10)
        self.model_names = []

    def listener_callback(self, msg):
        # This function runs in ROS2 thread
        # Example: msg.data contains model name
        if msg.data not in self.model_names:
            self.model_names.append(msg.data)
            print(f"Model received: {msg.data}")

class MainWindow(QWidget):
    def __init__(self, ros_node):
        super().__init__()
        self.ros_node = ros_node
        self.setWindowTitle("Gazebo Models Viewer")

        self.layout = QVBoxLayout(self)
        self.list_widget = QListWidget()
        self.refresh_button = QPushButton("Refresh Models")

        self.layout.addWidget(self.list_widget)
        self.layout.addWidget(self.refresh_button)

        self.refresh_button.clicked.connect(self.update_model_list)

        # Timer to periodically update GUI with ROS data
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_model_list)
        self.timer.start(1000)  # update every second

    def update_model_list(self):
        # Clear list and update with new data from ROS node
        self.list_widget.clear()
        for model in self.ros_node.model_names:
            self.list_widget.addItem(model)

def main():
    rclpy.init()
    ros_node = Ros2Listener()

    app = QApplication(sys.argv)
    window = MainWindow(ros_node)
    window.show()

    # To integrate rclpy spinning with PySide event loop,
    # we use QTimer to spin ROS once in main thread:
    def ros_spin():
        rclpy.spin_once(ros_node, timeout_sec=0)

    ros_timer = QTimer()
    ros_timer.timeout.connect(ros_spin)
    ros_timer.start(50)  # spin ROS every 50 ms

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
