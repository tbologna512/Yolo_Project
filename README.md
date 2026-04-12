# Yolo_Project (Software Engineering I Big Project)

Team project for Software Engineering I (OOAD/UML + iterative development).  
This repo contains code + UML artifacts for running a custom YOLO candy detector locally.

## Overview

Macro Manager is a computer vision system that detects packaged candy using a trained YOLO model and displays information such as product identity and confidence level.

The system has been iteratively developed throughout the semester, transitioning from an initial script-based implementation to a more structured object-oriented design.


## Contents
- `run_webcam.py` — run the trained YOLO model on a webcam or file
- `find_camera.py` — helper to identify camera indexes
- `macro_manager.py` — utility used to capture images for dataset expansion and training
- `use_case_diagram.puml` — PlantUML use case diagram
- `models/` — put model weights here (not committed)

## Getting started (follow these steps)
1) Clone this repo to your PC
2) Download the model from Releases (v1.0)
3) Set up the Anaconda environment + install dependencies
4) Run `run_webcam.py`

### Clone the repo
```text
git clone https://github.com/tbologna512/Yolo_Project.git
cd Yolo_Project
```

## Get the model weights
Model weights are distributed via **GitHub Releases** (not stored in the repo).
1) Go to **Releases**
2) Open **v1.0** and download `my_model.zip`
3) Extract and place `my_model.pt` here: `models/my_model.pt`

## Setup (Recommended: Anaconda)

### 1) Create and activate environment (run in Anaconda Prompt)
```text
conda create --name yolo-env1 python=3.12 -y
conda activate yolo-env1
```
### 2) Install dependencies (run in Anaconda Prompt)
```text
pip install -r requirements.txt
```
### 3) Optional: NVIDIA GPU acceleration ONLY IF YOU HAVE AN NVIDIA GPU (run in Anaconda Prompt)
```text
pip install --upgrade torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```
### 4) Verify CUDA (optional):
This checks whether PyTorch can see your NVIDIA GPU. If it prints `True`, your model can run on GPU for faster performance.

```text
python -c "import torch; print(torch.cuda.is_available()); print(torch.version.cuda)"
```
### 5) Run the detector (default camera is usb0)
```text
python run_webcam.py --model models/my_model.pt --source usb0
```
### If a different camera needed

```text
python run_webcam.py --model models/my_model.pt --source usb1
```
---

## Object-Oriented Design (Current Iteration)

The project has been refactored to follow an object-oriented design that aligns with the system’s UML diagrams and layered architecture.

The system is organized into the following layers:

- **UI Layer**
  - Handles user interaction and display (e.g., WebcamWindow)

- **Application Layer**
  - Coordinates workflows and system behavior (e.g., ScanController, CaptureController)

- **Domain Layer**
  - Represents core system data (e.g., Detection, BoundingBox, CandyProduct, TrainingImage)

- **Technical Services Layer**
  - Provides reusable services such as camera access, inference, and file storage (e.g., CameraService, YoloInferenceService, FileStorageService)

This structure improves modularity, maintainability, and alignment between design and implementation.

---

## Project Structure (OOP Refactor)

```
controllers/
    scan_controller.py
    capture_controller.py

domain/
    models.py

services/
    camera_service.py
    yolo_inference_service.py
    file_storage_service.py

run_webcam.py
macro_manager.py
find_camera.py
```
## Quick Run (OOP Version)

1. Open Anaconda Prompt
2. Navigate to the project folder:
   cd C:\SoftEngBigP

3. Activate the environment:
   conda activate yolo-env1

4. Run the webcam inference:
   python run_webcam.py --source usb1

5. (Optional) Run data collection:
   python macro_manager.py

## Iterative Development

This project was developed using an iterative approach. Early versions focused on quickly implementing functionality using script-based code.

Later iterations emphasized:
- UML modeling (domain model, sequence diagrams, communication diagrams, class diagrams)
- separation of concerns
- transition to object-oriented design

The current implementation reflects the intended design structure defined in the UML artifacts.

## Challenges and Constraints

- Limited initial experience with team collaboration using GitHub
- Difficulty balancing multiple projects and coordinating contributions
- Initial over-ambition of the system design (AI-based system)
- Early tendency toward a waterfall-style approach instead of iterative refinement
- Time constraints and scheduling conflicts among team members

As the semester progressed, the team improved by focusing on smaller iterations and aligning implementation with design artifacts.