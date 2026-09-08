# COUNTRIX: Real-Time-Object-Classification-Counting-System
Countrix is an object classification system that uses an ESP32-CAM, dual-band Wi-Fi antenna for stable feedback, Arduino UNO, LCD, Servo motors and YOLOv8n to detect, classify and count different classes of objects such as coins, screws, bolts, and nuts. 
The ESP32 provides live feedback to the custom-trained YOLOv8n object detection model to identify objects and locate them using bounding boxes.
Arduino communication enables the yolov8n model to interact with the physical hardware and relay the detection results to the LCD.
The yolov8n model was trained at (320x320) resolution using CUDA for GPU utilization. The training results peaked at 50 epochs(tested experimentally).
