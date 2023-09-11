
import os
# import cv2
# from ultralytics import YOLO
#
# # Initialize the YOLO model
# model_path = os.path.join('.', 'models', 'alpaca_detector.pt')
# model = YOLO(model_path)  # load a custom model
#
# threshold = 0.5
#
# class_name_dict = {0: 'alpaca'}
#
# # Initialize the webcam capture
# cap = cv2.VideoCapture(0)  # Use the default webcam (usually identified as 0)
#
# # Get the initial frame to determine its dimensions
# ret, frame = cap.read()
# H, W, _ = frame.shape
#
# # Initialize the video writer for output
# out = cv2.VideoWriter('output_webcam.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 30, (W, H))
#
# while True:  # Infinite loop to continuously capture frames
#     ret, frame = cap.read()
#
#     # Perform object detection using the YOLO model
#     results = model(frame)[0]
#
#     for result in results.boxes.data.tolist():
#         x1, y1, x2, y2, score, class_id = result
#
#         if score > threshold:
#             # Draw bounding boxes and labels on the frame
#             cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
#             cv2.putText(frame, class_name_dict[int(class_id)].upper(), (int(x1), int(y1 - 10)),
#                         cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
#
#     # Write the annotated frame to the output video
#     out.write(frame)
#
#     # Display the processed frame in a window
#     cv2.imshow('Webcam Object Detection', frame)
#
#     # Exit the loop if the 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Release the webcam capture and video writer objects
# cap.release()
# out.release()
# cv2.destroyAllWindows()
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import cv2
from ultralytics import YOLO

# Initialize the webcam capture (default webcam, index 0)
cap = cv2.VideoCapture(0)

# Initialize the YOLO model (provide the path to your YOLO model file)
model_path = os.path.join('.', 'models', 'yolov8n.pt')
model = YOLO(model_path)  # load a custom model

threshold = 0.5

class_name_dict = {0: 'prince chodu'}

# Create a video writer to save the processed video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # Adjust frame size and frame rate as needed

while True:
    ret, frame = cap.read()

    # Check if the frame was successfully captured
    if not ret:
        break

    results = model(frame)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score >= threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, class_name_dict[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

    # Write the annotated frame to the output video
    out.write(frame)

    # Display the processed frame
    cv2.imshow('Object Detection', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and video writer, and close any OpenCV windows
cap.release()
out.release()
cv2.destroyAllWindows()
