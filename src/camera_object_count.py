"""
camera_object_count.py
Real-time Object Detection + Counting using YOLOv8 + OpenCV
Default resolution: 640x480
"""

from ultralytics import YOLO
import cv2
import numpy as np
from collections import Counter
from utils.draw_utils import draw_side_panel

# Load YOLOv8 nano model (will download if not present)
model = YOLO("yolov8n.pt")

# Open default camera
cap = cv2.VideoCapture(0)
# Set resolution to 640x480 for performance
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

print("Camera opened. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection (pass the frame directly)
    results = model(frame, verbose=False)
    annotated = results[0].plot()  # draw bounding boxes on frame

    # Collect detected class names
    names = model.names
    detected = [names[int(cls)] for cls in results[0].boxes.cls] if len(results[0].boxes) > 0 else []
    counts = Counter(detected)

    # Draw side panel and combine
    panel_width = 320
    combined = draw_side_panel(annotated, counts, panel_width=panel_width)

    cv2.imshow("OJD_ObjectDetection - Detection & Counting", combined)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
