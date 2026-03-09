import cv2

img=cv2.imread('picture1.png')

cv2.imshow("Picture",img)
cv2.waitKey(0)
cv2.destroyAllWindows()