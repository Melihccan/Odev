import cv2
import numpy as np

img = cv2.imread("image.jpg")

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([0,70,50])
upper_red = np.array([10,255,255])

red_mask = cv2.inRange(img_hsv, lower_red, upper_red)

res = cv2.bitwise_and(img,img, mask= red_mask)

cv2.imshow("Image", img)
cv2.imshow("Red Mask", red_mask)
cv2.imshow("Result", res)
cv2.waitKey(0)
cv2.destroyAllWindows()