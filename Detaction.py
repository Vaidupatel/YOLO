# '''code link:https://www.freecodecamp.org/news/how-to-detect-objects-in-images-using-yolov8/'''
# '''code link:https://www.freecodecamp.org/news/how-to-detect-objects-in-images-using-yolov8/'''


from ultralytics import YOLO
import cv2

# Load the YOLOv8 model with the best weights
model = YOLO(r'C:\Users\admin\OneDrive - oxyguard\Project F\yolo_v8-main\runs\detect\train\weights\last.pt')

# Open a connection to your webcam (usually 0 or 1 for built-in webcam)
cap = cv2.VideoCapture("http://192.168.29.109:4747/video")

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        break

    # Perform object detection on the frame
    results = model.predict(source=frame, show = True)

    # Get the first result
    result = results[0]

    # Check if any objects were detected
    if len(result.boxes) > 0:
        # Extract information about the first detected object
        box = result.boxes[0]
        cords = box.xyxy[0].tolist()
        conf = box.conf[0].item()
        class_id = result.names[box.cls[0].item()]

        print("Object type:", class_id)
        print("Coordinates:", cords)
        print("Probability:", conf)

    # Display the frame with bounding boxes
    # result.show()

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()


# Load your YOLO model
model = YOLO(r'C:\Users\admin\OneDrive - oxyguard\Project F\yolo_v8-main\runs\detect\train\weights\last.pt')

# Open a connection to your webcam (usually webcam index 0, but it may vary)
cap = cv2.VideoCapture("http://192.168.29.109:4747/video")

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Make sure the frame was read successfully
    if not ret:
        break

    # Perform object detection on the frame
    results = model.predict(source=frame, show = True)

    # Get the first result (assuming there's only one frame)
    result = results[0]

    # Loop through detected objects
    for box in result.boxes:
        class_id = result.names[box.cls[0].item()]
        cords = box.xyxy[0].tolist()
        cords = [round(x) for x in cords]
        conf = round(box.conf[0].item(), 2)
        print("Object type:", class_id)
        print("Coordinates:", cords)
        print("Probability:", conf)
        print("---")

    # Display the frame with bounding boxes (you can customize this part)
    result.show()
# 202103103520
    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()
