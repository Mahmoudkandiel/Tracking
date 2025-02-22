# Object Tracking using OpenCV



## Description
This system implements real-time webcam tracker .Users selects ROI using Bounding BOX, and the system will track the object.the project is designed to be very simple.


## Tracker

- CSRT Tracker is used in this project, Since it have the best accuracy among other trackers

## Installation

install the dependencies

```bash
pip install -r requirements.txt
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


2-Main(`main.py`):


3-Tracker(`tracker.py`):


## Reference

ROI BB selscting live : (https://stackoverflow.com/questions/68969235/select-roi-on-video-stream-while-its-playing)

