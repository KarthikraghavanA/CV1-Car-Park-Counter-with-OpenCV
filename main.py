import cv2
import numpy as np
import pickle
import cvzone

vid1 = cv2.VideoCapture('carPark.mp4')


with open('carParkPosition.txt', 'rb') as f:
    posList = pickle.load(f)

height = 240 - 193
width = 157 - 50

def check_Parking_space(imgPro):
    spaceCounter = 0
    for pos in posList:

        x,y = pos
        # cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height),(32, 26, 217),3)
        cv2.imshow('Image', img)

        imgCrop = imgPro[y:y+height, x:x+width]
        cv2.imshow(str(x*y), imgCrop)

        count = cv2.countNonZero(imgCrop) # Count pixels
        cvzone.putTextRect(img, str(count), (x,y+height -2), scale=1, thickness=1,offset=0, colorR=(0,0,255))

        if count < 500:
            color = (0,255,0)
            thickness = 4
            spaceCounter += 1
        else:
            color = (0,0,255)
            thickness = 2
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
    cvzone.putTextRect(img, f'FREE {str(spaceCounter)} / {len(posList)}', (400,80),scale=3, thickness=5,offset=20, colorR=(0,200,0))


while True:
    if vid1.get(cv2.CAP_PROP_POS_FRAMES) == vid1.get(cv2.CAP_PROP_FRAME_COUNT):
        vid1.set(cv2.CAP_PROP_POS_FRAMES,0)

    success, img = vid1.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 1)
    imgThreshold = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                          cv2.THRESH_BINARY_INV,25,16)
    imgMedian = cv2.medianBlur(imgThreshold, 5) # Removes some noise
    kernel = np.zeros((3,3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel=kernel, iterations=1) # Makes lines thicker

    check_Parking_space(imgDilate)
    # for pos in posList:
    #     x,y = pos
        # cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (32, 26, 217), 3)

    cv2.imshow('Image', img)
    # cv2.imshow('Image blur', blur)
    # cv2.imshow('Image Threshold', imgThreshold)
    # cv2.imshow('Image Median', imgMedian) # Removes noise
    # cv2.imshow('Image Dilate', imgDilate)

    cv2.waitKey(1)

# No pixels --> No car