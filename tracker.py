import cv2


tracker = cv2.TrackerCSRT_create()
#tracker = cv2   .TrackerMIL_create()
cap = cv2.VideoCapture(0)

cv2.namedWindow('Frame')
if not cap.isOpened():
    exit()

# ROI defining Points
p1, p2 = (0, 0), (0, 0)
drawing = False  
show_drawing = False
blue = (255, 0, 0)
red = (0, 0, 255)


def on_mouse(event, x, y, flags, userdata):
    global p1, p2, drawing, show_drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        show_drawing = True
        p1 = x, y
        p2 = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            p2 = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        p2 = x, y



cv2.setMouseCallback('Frame', on_mouse)
track_on = False
while True:
    val, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if not val:
        break

    if show_drawing and not track_on:
        p2 = (
            0 if p2[0] < 0 else (p2[0] if p2[0] < frame.shape[1] else frame.shape[1]),
            0 if p2[1] < 0 else (p2[1] if p2[1] < frame.shape[0] else frame.shape[0])
        )
        text = f"{p1}, {p2}"
        cv2.rectangle(frame, p1, p2, blue, 3)
        cv2.putText(frame, "Initialize Tracker", (p1[0],p1[1]), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,(0,0,0),2)
        
    if track_on:
        track , bbox = tracker.update(frame)
        if track:
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, red, 3)
            cv2.putText(frame, "Tracking ON", (p1[0],p1[1]), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,(0,0,0),2)

            

            
        else:
            track_on = False

    cv2.imshow('Frame', frame)

    pressed = cv2.waitKey(1)
    if pressed in [13, 32]:
        drawing = False
        show_drawing = True
        bbox = (p1[0], p1[1], p2[0]-p1[0], p2[1]-p1[1])
        track = tracker.init(frame, bbox)
        track_on = True
        

        # here do something with ROI points values (p1 and p2)
    elif pressed in [ord('c'), ord('C'), 27]:
        # Pressed C or Esc to cancel ROI
        drawing = False
        show_drawing = False
    elif pressed in [ord('s'), ord('S')]:
        cv2.setMouseCallback('Frame', on_mouse)
        drawing = False
        show_drawing = False
        track_on = False
    elif pressed in [ord('q'), ord('Q')]:
        break 
    
    


cap.release()
cv2.destroyAllWindows()