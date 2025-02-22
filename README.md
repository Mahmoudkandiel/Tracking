# Object Tracking using OpenCV

![ezgif-551b988f72242c](https://github.com/user-attachments/assets/5ae82574-c125-4109-9b64-a95200b37d98)



## Description
This system implements real-time webcam tracker .Users selects ROI using Bounding BOX, and the system will track the object.the project is designed to be very simple.


## Tracker

- CSRT Tracker is used in this project, Since it have the best accuracy among other trackers
- The CSRT algorithm utilizes color channel information to handle appearance changes caused by illumination variations. It models the target object using color features to enhance tracking accuracy. Spatial Reliability: Spatial reliability is employed to handle occlusions and non-rigid deformations

## Installation

install the dependencies

```bash
git clone https://github.com/Mahmoudkandiel/Tracking # clone
cd Tracking
pip install -r requirements.txt  # install
```

## Usage

Run the script using :

```bash
python main.py
```

### Key Controls

- **Select the Object:** click and drag to select ROI
- **Start Tracking:** press `enter` to start tracking
- **Reset Tracking:** press `R` to start tracking
- **Quit:** press `Q`

## Code Explanation

This project consists of three main components:

1- Ui Class(`ui.py`) :

- Responsible for User interface
- Handling Mouse and keyboard interactions


2-Main(`main.py`)

-used to Run the program

3-Tracker(`tracker.py`):

  -utlizes the CSRT tracker in opencv library


## Reference

ROI BB selscting live : (https://stackoverflow.com/questions/68969235/select-roi-on-video-stream-while-its-playing)

