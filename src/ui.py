import cv2
from tracker import Tracker
from config import TRACK_COLOR, INIT_COLOR,INIT_TEXT, START_TEXT_1, START_TEXT_2, START_TEXT_3, TEXT_COLOR,TRACK_TEXT


class UI():
    def __init__(self):
        self.tracker = Tracker()
        self.is_tracking = False
        self.drawing = False
        self.show_drawing = False
        self.bbox = None
        self.p1, self.p2  = (0, 0), (0, 0)
        self.frame = None
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Error: Could not open camera.")
            exit()
        cv2.namedWindow('Frame')
        cv2.setMouseCallback('Frame', self.on_mouse)




    def on_mouse(self, event, x, y, flags, userdata):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.show_drawing = True
            self.p1 = x, y
            self.p2 = x, y
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing:
                self.p2 = x, y
        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            self.p2 = x, y

    def start_tracking(self):
        cv2.setMouseCallback('Frame', self.on_mouse)
        self.track_on = False
        while True:
            val, self.frame = self.cap.read()
            self.frame = cv2.flip(self.frame, 1)
            if not val:
                break
            
            if not self.track_on:
                    cv2.putText(self.frame,START_TEXT_1 , (10,20), cv2.FONT_HERSHEY_TRIPLEX, 0.8,TEXT_COLOR,2)
                    cv2.putText(self.frame,START_TEXT_2 , (10,50), cv2.FONT_HERSHEY_TRIPLEX, 0.8,TEXT_COLOR,2)
                    cv2.putText(self.frame,START_TEXT_3 , (10,80), cv2.FONT_HERSHEY_TRIPLEX, 0.8,TEXT_COLOR,2)


            if self.show_drawing and not self.track_on:
                self.p2 = (
                    0 if self.p2[0] < 0 else (self.p2[0] if self.p2[0] < self.frame.shape[1] else self.frame.shape[1]),
                    0 if self.p2[1] < 0 else (self.p2[1] if self.p2[1] < self.frame.shape[0] else self.frame.shape[0])
                )
                text = f"{self.p1}, {self.p2}"
                cv2.rectangle(self.frame, self.p1,self.p2, INIT_COLOR, 3)
                cv2.putText(self.frame, INIT_TEXT, (self.p1[0],self.p1[1]), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,TEXT_COLOR,2)


            if self.track_on:
                track , bbox = self.tracker.update(self.frame)
                if track:
                    self.p1 = (int(bbox[0]), int(bbox[1]))
                    self.p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                    cv2.rectangle(self.frame, self.p1, self.p2, TRACK_COLOR, 3)
                    cv2.putText(self.frame, TRACK_TEXT, (self.p1[0],self.p1[1]), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,TEXT_COLOR,2)
                else:
                    self.track_on = False
                    

            cv2.imshow('Frame', self.frame)

            pressed = cv2.waitKey(1)
            if pressed in [13, 32]:
                    self.drawing = False
                    self.show_drawing = True
                    self.bbox = (self.p1[0], self.p1[1], self.p2[0]-self.p1[0], self.p2[1]-self.p1[1])
                    self.tracker.initialize(self.frame, self.bbox)
                    self.track_on = True
            elif pressed in [ord('r'), ord('R')]:
                cv2.setMouseCallback('Frame', self.on_mouse)
                self.drawing = False
                self.show_drawing = False
                self.track_on = False
            elif pressed in [ord('q'), ord('Q')]:
                break 
                
                


        self.cap.release()
        cv2.destroyAllWindows()




