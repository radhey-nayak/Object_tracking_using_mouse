"""Author : Radhashyam Nayak
   Date   : 12 | jun | 2020
"""

import cv2

# cap = cv2.VideoCapture(0) # for cam
cap = cv2.VideoCapture('vtest.avi')  # for video
while True:
    success, img = cap.read()
    cv2.putText(img, "When You Ready Press 's' ", (100, 100), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (255, 23, 100), 2)
    cv2.imshow('Tracking', img)
    if cv2.waitKey(80) & 0xFF == ord('s'):
        break
# install opencv-contrib-python
# Trackers
# tracker = cv2.TrackerMOSSE_create()  # high speed & low accuracy
tracker = cv2.TrackerCSRT_create()  # low speed & high accuracy
# tracker = cv2.TrackerGOTURN_create() # some error
# tracker = cv2.TrackerMedianFlow_create()  # working accurate
# tracker = cv2.TrackerTLD_create() #working
# tracker = cv2.TrackerKCF_create() #working
# tracker = cv2.TrackerMIL_create()
# tracker = cv2.TrackerBoosting_create()
success, img = cap.read()
bbox = cv2.selectROI('Tracking', img, True)
tracker.init(img, bbox)


def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3, 1)
    cv2.putText(img, 'Tracking', (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)


while True:
    timer = cv2.getTickCount()
    success, img = cap.read()

    success, bbox = tracker.update(img)

    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img, 'Lost', (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    cv2.putText(img, str(int(fps)), (75, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.imshow('Tracking', img)

    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
