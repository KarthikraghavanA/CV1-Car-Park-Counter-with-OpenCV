import cv2
import pickle

height = 240 - 193
width = 157 - 50

try:
    with open('carParkPosition.txt', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []

def mouseClick(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
    if event == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1,y1 = pos
            if x1<x<x+width and y1<y<y+height:
                posList.pop(i)

    with open('carParkPosition.txt', 'wb') as f:
        pickle.dump(posList, f)

while True:
    img = cv2.imread('Carpark.png')
    cv2.rectangle(img, (50, 193), (157, 240), (32, 26, 217), 1) #BGR # Create Rectangle for the parking spaces

    for pos in posList:
        cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height),(32, 26, 217),1)
    cv2.imshow('Image', img)

    cv2.setMouseCallback('Image', mouseClick)
    cv2.waitKey(1)


