import cv2
from PIL import Image
from utils import get_limits

green = [255, 255, 0]

cap = cv2.VideoCapture(1)   # Camera index
cap.set(3, 1000)    # Webcam width
cap.set(4, 600)     # Webcam height

while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Getting the range of a color
    lowerLimit, upperLimit = get_limits(color=green)
    # Creating a mask
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
    mask_ = Image.fromarray(mask)
    
    # Displaying bounding box on the detected mask/color
    bbox = mask_.getbbox()
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 2)

    cv2.imshow('Color Detector', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()