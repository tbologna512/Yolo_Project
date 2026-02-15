# Yolo_Project (Software Engineering I Big Project)

Team project for Software Engineering I (OOAD/UML + iterative development).  
This repo contains code + UML artifacts for running a custom YOLO candy detector locally.

## Contents
- `run_webcam.py` — run the trained YOLO model on a webcam or file
- `find_camera.py` — helper to identify camera indexes
- `macro_manager.py` — utility used to capture images for dataset expansion
- `use_case_diagram.puml` — PlantUML use case diagram
- `models/` — put model weights here (not committed)

## Get the model weights
Model weights are distributed via **GitHub Releases** (not stored in the repo).
1) Go to **Releases**
2) Download `my_model.zip`
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
### 3) Optional: NVIDIA GPU acceleration (only if you have an NVIDIA GPU)
```text
pip install --upgrade torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```
### 4) Verify CUDA (optional):
This checks whether PyTorch can see your NVIDIA GPU. If it prints True, your model can run on GPU for faster performance.

```text
python -c "import torch; print(torch.cuda.is_available()); print(torch.version.cuda)"
```
### 5) Run the detector (default camera is usb0)
```text
python run_webcam.py --model models/my_model.pt --source usb0
```
### If a different camera wanted

```text
python run_webcam.py --model models/my_model.pt --source usb1
```