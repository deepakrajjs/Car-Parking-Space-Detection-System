import cv2
import pickle
import cvzone
import numpy as np

# Load parking position list (you should have ParkingPos file with predefined positions)
with open('ParkingPos', 'rb') as f:
    posList = pickle.load(f)

# Width and Height of each parking spot (adjust accordingly)
width, height = 107, 48

# Video feed (Replace with your parking video or image sequence)
cap = cv2.VideoCapture('carPark.mp4')

def checkParkingSpace(imgPro):
    spaceCounter = 0

    for pos in posList:
        x, y = pos
        imgCrop = imgPro[y:y + height, x:x + width]
        count = cv2.countNonZero(imgCrop)

        # Threshold - adjust this based on your environment
        if count < 900:
            color = (0, 255, 0)   # Green for available
            thickness = 5
            spaceCounter += 1
        else:
            color = (0, 0, 255)   # Red for occupied
            thickness = 2

        # Draw rectangle around each parking space
        cv2.rectangle(img, pos, (x + width, y + height), color, thickness)

    # Display available spaces count
    cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (50, 50), scale=2, thickness=3, offset=10, colorR=(0, 200, 0))

while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()

    # Preprocessing
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThresh = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThresh, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    # Check parking spaces
    checkParkingSpace(imgDilate)

    # Display
    cv2.imshow("Image", img)
    cv2.waitKey(10)
