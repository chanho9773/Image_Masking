# 소벨 필터

import cv2
import numpy as np

img = cv2.imread('DrivingRoad.jpg')

# built-in 소벨 필터
edge_gx = cv2.Sobel(img, -1, 1, 0, ksize=3)
edge_gy = cv2.Sobel(img, -1, 0, 1, ksize=3)

# 결과 출력
merged = np.hstack((img, edge_gx+edge_gy))
cv2.imshow('sobel', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()