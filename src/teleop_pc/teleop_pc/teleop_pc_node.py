#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import threading
import sys

class TeleopPCNode(Node):
    def __init__(self):
        super().__init__("teleop_pc_node")
        self.logger = self.get_logger()
        self.publisher = self.create_publisher(String, "teleop_commands", 100)
        self.lock = threading.Lock()
        self.quit = False

    def key_callback(self):
        # Capture keyboard input and publish it
        while not self.quit:
            key = input("Enter teleop command: ").lower()

            # Input validation
            valid_keys = {'w', 's', 'a', 'd', 'e', 'r', 'q'}
            if key in valid_keys:
                msg = String()
                msg.data = key
                with self.lock:
                    self.publisher.publish(msg)
            else:
                print("Invalid key. Please enter a valid teleop command.")

    def shutdown_callback(self, signal):
        print("Shutting down...")
        self.quit = True

def main(args=None):
    rclpy.init(args=args)
    node = TeleopPCNode()

    print("WELCOME TO WAVEGO TELEOP NODE:")
    print("Press 'W' to move forward, 'S' to move backward, 'A' to turn left, 'D' to turn right.")
    print("Press'E' to stop Forward/BAckward move or 'R' to stop turn left/right move.")
    print("Press 'Q' to quit the program.")
    print("----------------------------------------------------------------------------------------------------------------")

    # Run the key capture in a separate thread
    thread = threading.Thread(target=node.key_callback)
    thread.start()

    rclpy.spin(node)

    # Ensure the thread is stopped before exiting
    thread.join()

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

