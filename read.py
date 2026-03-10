import cv2

img=cv2.imread('picture2.png')
resize=cv2.resize(img,(500,500))
gray=cv2.cvtColor(resize,cv2.COLOR_BGR2GRAY)

cv2.imshow("original",resize)
cv2.imshow("gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
#print(img.shape)
# cv2.imshow("Picture",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()