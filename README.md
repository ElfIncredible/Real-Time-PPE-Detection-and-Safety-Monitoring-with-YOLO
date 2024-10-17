# Real-Time PPE Detection and Safety Monitoring with YOLO
This project utilizes the YOLO (You Only Look Once) object detection model to monitor and detect the presence of personal protective equipment (PPE) in real-time. It identifies safety compliance by detecting items such as hardhats, safety vests, and masks, as well as flagging violations like missing PPE. The system processes video input, drawing bounding boxes around detected objects, and color-codes them to differentiate between safe and unsafe conditions. This solution is designed for real-time monitoring in industrial and construction environments to enhance workplace safety.

## Table of Contents
- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Dataset](#dataset)
- [Computer Vision](#computer-vision)

## Project Overview
**Overview:** This project aims to enhance safety at construction sites by automatically detecting safety gear violations using computer vision techniques. Utilizing the YOLOv8 (You Only Look Once) object detection model, the system identifies personnel and safety equipment such as hardhats, safety vests, and masks. It also flags safety violations like the absence of required gear. This solution can be deployed in real-time to monitor construction sites and ensure compliance with safety protocols.

**Objective:** To develop a machine learning model capable of detecting and classifying objects related to construction site safety, identifying violations such as missing hardhats, safety vests, or masks, and providing real-time alerts for corrective actions.

** Methodology:**
YOLOv8: The model architecture used for real-time object detection.
Training: The model is trained on the construction site dataset for 50 epochs with an image size of 640x640 pixels.
Video Processing: The model processes video feeds from construction sites, identifying workers and their compliance with safety gear requirements.
Visualization: Bounding boxes and class labels are drawn on the video feed, with color-coded indicators:
Green: Proper safety equipment worn (e.g., hardhat, mask, safety vest)
Red: Safety violations (e.g., no hardhat, no mask, no vest)
Blue: Other objects like machinery and vehicles

**Technology Stack:**
- Python
- YOLOv8 for object detection
- OpenCV and CVZone for video processing
- Roboflow for dataset management

## Problem Statement
Ensuring safety compliance at construction sites is a critical concern, as failure to wear proper safety gear can lead to severe accidents, injuries, and even fatalities. Current methods of monitoring safety compliance often rely on manual inspection, which is time-consuming, error-prone, and not feasible for continuous real-time monitoring. With large and complex construction sites, it becomes increasingly challenging to ensure that all workers are adhering to safety protocols, such as wearing hardhats, safety vests, and masks.

There is a need for an automated system that can reliably and efficiently detect safety gear violations in real time, minimizing the risk of human error and improving safety outcomes. Such a system should be capable of identifying workers, detecting the presence or absence of required safety equipment, and providing immediate feedback for corrective action. This would help construction managers enforce safety regulations, reduce the occurrence of accidents, and ensure a safer working environment.

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
