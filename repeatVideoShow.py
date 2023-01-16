# Method 1 - To make the video loop

import cv2

vid1 = cv2.VideoCapture('carPark.mp4')

while(vid1.isOpened()):
    ret, frame = vid1.read()

    if ret:
        cv2.imshow('frame',frame)
    else:
        vid1.set(cv2.CAP_PROP_POS_FRAMES, 0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid1.release()
cv2.destroyAllWindows()

# Method 2 -To make the video loop

while True:
    if vid1.get(cv2.CAP_PROP_POS_FRAMES) == vid1.get(cv2.CAP_PROP_FRAME_COUNT):
        vid1.set(cv2.CAP_PROP_POS_FRAMES,0)