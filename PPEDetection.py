from ultralytics import YOLO  # Import the YOLO model from the ultralytics library
import cv2  # for video and image processing
import cvzone  # for additional computer vision utilities
import math  # for calculations

cap = cv2.VideoCapture(0) # For Webcam
cap.set(3, 1280)  # Set the width of the webcam capture to 1280
cap.set(4, 720)  # Set the height of the webcam capture to 720

#cap = cv2.VideoCapture("../Videos/ppe-3-1.mp4")  # For loading a video file instead of webcam

# Load the pre-trained YOLO model
model = YOLO("ppe.pt")

# Define the class names for the objects the model will detect
classNames = ['Hardhat', 'Mask', 'NO-Hardhat', 'NO-Mask', 'NO-Safety Vest', 'Person', 'Safety Cone', 'Safety Vest', 'machinery', 'vehicle']

# Default color for detected objects (Red)
myColor = (0, 0, 255)

# Loop for reading each frame from the video
while True:
    success, img = cap.read()  # Capture a frame from the video
    results = model(img, stream=True)  # Perform object detection on the current frame

    # Iterate through the results of the detection
    for r in results:
        boxes = r.boxes  # Get the detected boxes (bounding boxes)

        # Iterate through each box (detected object)
        for box in boxes:
            # Get the coordinates of the bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # Convert to integer values
            # cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)  # Uncomment to draw rectangles

            w, h = x2 - x1, y2 - y1  # Calculate the width and height of the bounding box
            # cvzone.cornerRect(img, (x1, y1, w, h))  # Draw a fancy corner rectangle (if desired)

            # Get the confidence of the detection
            conf = math.ceil((box.conf[0] * 100)) / 100  # Round the confidence score to 2 decimal places

            # Get the class label of the detected object
            cls = int(box.cls[0])  # Class index (integer)
            currentClass = classNames[cls]  # Convert class index to class name
            print(currentClass)  # Print the detected class to the console

            # Only display objects with a confidence score above 0.5
            if conf > 0.5:
                # Set the color based on whether the object is a safety violation or not
                if currentClass == 'NO-Hardhat' or currentClass == 'NO-Safety Vest' or currentClass == 'NO-Mask':
                    myColor = (0, 0, 255)  # Red for safety violations
                elif currentClass == 'Hardhat' or currentClass == 'Safety Vest' or currentClass == 'Mask':
                    myColor = (0, 255, 0)  # Green for proper safety equipment
                else:
                    myColor = (255, 0, 0)  # Blue for other objects

                # Display the class name and confidence score on the frame
                cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)),
                                   scale=1, thickness=1, colorB=myColor, colorT=(255, 255, 255), colorR=myColor, offset=5)
                # Draw the bounding box around the detected object
                cv2.rectangle(img, (x1, y1), (x2, y2), myColor, 3)

    # Display the image with detections in a window
    cv2.imshow("Image", img)
    cv2.waitKey(1)  # Wait for 1 ms between frames
