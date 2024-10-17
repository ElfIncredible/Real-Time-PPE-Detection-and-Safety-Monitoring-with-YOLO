# Real-Time PPE Detection and Safety Monitoring with YOLO
This project utilizes the YOLO (You Only Look Once) object detection model to monitor and detect the presence of personal protective equipment (PPE) in real-time. It identifies safety compliance by detecting items such as hardhats, safety vests, and masks, as well as flagging violations like missing PPE. The system processes video input, drawing bounding boxes around detected objects, and color-codes them to differentiate between safe and unsafe conditions. This solution is designed for real-time monitoring in industrial and construction environments to enhance workplace safety.

## Table of Contents
- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Dataset](#dataset)
- [Computer Vision](#computer-vision)
- [Results](#results)
- [Impact](#impact)
- [Further Improvements](#further-improvements)

## Project Overview
**Overview:** This project aims to enhance safety at construction sites by automatically detecting safety gear violations using computer vision techniques. Utilizing the YOLOv8 (You Only Look Once) object detection model, the system identifies personnel and safety equipment such as hardhats, safety vests, and masks. It also flags safety violations like the absence of required gear. This solution can be deployed in real-time to monitor construction sites and ensure compliance with safety protocols.

**Objective:** To develop a machine learning model capable of detecting and classifying objects related to construction site safety, identifying violations such as missing hardhats, safety vests, or masks, and providing real-time alerts for corrective actions.

**Methodology:** 

- **YOLOv8:** The model architecture used for real-time object detection.
- **Training:** The model is trained on the construction site dataset for 50 epochs with an image size of 640x640 pixels.
- **Video Processing:** The model processes video feeds from construction sites, identifying workers and their compliance with safety gear requirements.
- **Visualization:** Bounding boxes and class labels are drawn on the video feed, with color-coded indicators:
  - **Green:** Proper safety equipment worn (e.g., hardhat, mask, safety vest)
  - **Red:** Safety violations (e.g., no hardhat, no mask, no vest)
  - **Blue:** Other objects like machinery and vehicles

**Technology Stack:**
- Python
- YOLOv8 for object detection
- OpenCV and CVZone for video processing
- Roboflow for dataset management

## Problem Statement
Ensuring safety compliance at construction sites is a critical concern, as failure to wear proper safety gear can lead to severe accidents, injuries, and even fatalities. Current methods of monitoring safety compliance often rely on manual inspection, which is time-consuming, error-prone, and not feasible for continuous real-time monitoring. With large and complex construction sites, it becomes increasingly challenging to ensure that all workers are adhering to safety protocols, such as wearing hardhats, safety vests, and masks.

There is a need for an automated system that can reliably and efficiently detect safety gear violations in real-time, minimizing the risk of human error and improving safety outcomes. Such a system should be capable of identifying workers, detecting the presence or absence of required safety equipment, and providing immediate feedback for corrective action. This would help construction managers enforce safety regulations, reduce the occurrence of accidents, and ensure a safer working environment.

## Dataset
The model is trained using the [Construction Site Safety Dataset](https://universe.roboflow.com/roboflow-universe-projects/construction-site-safety/dataset/27), which includes labeled images of construction workers with and without safety gear. The dataset consists of classes such as:
- Hardhat
- Mask
- No Hardhat
- No Mask
- No Safety Vest
- Safety Cone
- Machinery
- Vehicle
- Person

## Computer Vision
### Environment Setup
**GPU Initialization:**
- !nvidia-smi is used to check the availability and status of the GPU for model training and inference.

**Package Installation:**
- The command !pip install ultralytics installs the required package for the YOLO model.

### Model Inference
**Model Loading and Prediction:**
-The command !yolo task=detect mode=predict model=yolov8l.pt conf=0.25 source='https://ultralytics.com/images/bus.jpg' performs object detection on a sample image to demonstrate the model’s capabilities.

### Model Training
- **Training the YOLO Model:**
  - The command !yolo task=detect mode=train model=yolov8l.pt data=../content/drive/MyDrive/Datasets/ConstructionSiteSafetyYolov8/data.yaml epochs=50 imgsz=640 trains the YOLO model on the construction site safety dataset for 50 epochs, with image sizes set to 640x640 pixels.

### Video Processing Setup
**Importing Libraries:**
- Necessary libraries like cv2 for image processing, cvzone for additional utilities, and math for calculations are imported.

**Video Capture Initialization:**
- The code initializes video capture from a file (ppe-1-1.mp4) to process video frames for safety gear detection.

### Model Loading
- **Loading the Trained Model:**
  - The pre-trained model ppe.pt is loaded for detecting safety equipment in the video frames.

### Detection Loop
- **Frame Processing:**
  - A loop is established to continuously read frames from the video.
  - For each frame, the model performs object detection.

- **Bounding Box Extraction:**
  - Detected bounding boxes and their coordinates are extracted, and the detection confidence score is calculated.

### Object Classification
- **Class Detection and Confidence Filtering:**
  - The class names are defined, and the model checks for each detected object’s confidence score.
  - Objects with a confidence score above 0.5 are processed for visualization.

### Visualization
- **Drawing Bounding Boxes:**
  - The code uses color coding to indicate compliance:
    - **Red** for safety violations (e.g., missing hardhat or mask).
    - **Green** for proper safety gear.
    - **Blue** for other detected objects.
  - Class names and confidence scores are displayed on the video frames.

### Output Display
- **Displaying Processed Frames:**
  - The processed video frames with detections are displayed in a window, allowing real-time monitoring of safety compliance.

### Continuous Monitoring
- **Real-time Update:**
  - The loop runs indefinitely, updating the output window with each processed frame until manually stopped.
 
## Results
The YOLOv8 object detection model has demonstrated high effectiveness in monitoring construction site safety, achieving over 90% accuracy in detecting safety gear such as hardhats, safety vests, and masks. The system provides immediate feedback, enabling quick corrective actions and reducing the need for manual inspections.

## Impact
- **Enhanced Safety Compliance:** The automated system helps minimize workplace accidents, promoting a culture of safety.
- **Cost Savings:** Reducing accidents leads to lower medical costs, insurance claims, and potential legal liabilities, which can result in decreased insurance premiums.
- **Increased Productivity:** By freeing up resources from manual inspections, construction managers can focus on improving project efficiency.
- **Scalability:** The solution can be easily implemented across multiple sites, standardizing safety compliance monitoring.
- **Data-Driven Insights:** The system generates valuable data on safety trends, allowing for targeted training and risk assessment.

This project leverages technology to improve safety standards in the construction industry, contributing to a safer and more efficient work environment.

## Further Improvements
- **Model Optimization:**
  - **Fine-tuning the Model:** Continuously update the YOLOv8 model with new data to improve accuracy and adaptability to different site conditions.

- **Real-time Alerts:**
  - **Integration with Alert Systems:** Implement a system that sends immediate notifications to supervisors and workers when safety violations are detected, facilitating quicker responses.

- **Multi-camera Setup:**
  - **Expanded Coverage:** Utilize multiple cameras to provide comprehensive monitoring of the site, reducing blind spots and ensuring all areas are monitored effectively.

- **User Interface Enhancements:**
  - **Dashboard Development:** Create a user-friendly dashboard to display real-time compliance data and historical trends, empowering managers to make informed decisions.

- **Data Analytics:**
  - **Advanced Analytics:** Employ machine learning techniques to analyze detected violations and uncover patterns, enabling targeted interventions and improving safety compliance.


