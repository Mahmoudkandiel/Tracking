import cv2

class Tracker():
    
    def __init__(self):
        self.tracker = cv2.TrackerCSRT_create()

    def initialize(self, frame, bbox):
        return self.tracker.init(frame, bbox)

    def update(self,frame):
        return self.tracker.update(frame)
    
    
    

