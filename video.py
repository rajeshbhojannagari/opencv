# import cv2
# cap=cv2.VideoCapture('video1.mp4')
# while True:
#     ret,frame=cap.read()
#     if not ret:
#         break
#     gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     cv2.imshow("original",frame)
#     cv2.imshow("gray",gray)
#     if cv2.waitKey(25) & 0xFF==ord('q'):
#         break
# width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# fps=cap.get(cv2.CAP_PROP_FPS)
# print(width,height,fps)
# cap.release()
# cv2.destroyAllWindows()

import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("camera",gray)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()