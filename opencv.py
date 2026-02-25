import cv2

# img=cv2.imread("picture1.png")

# cv2.imshow("Image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cap=cv2.VideoCapture(0)
while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        break
    cv2.imshow("Camera",frame)
    key=cv2.waitKey(1) & 0xFF
    if key==ord('q') or key==27:
        break

cap.release()
cv2.destroyAllWindows()
