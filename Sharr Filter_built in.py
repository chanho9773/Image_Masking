# 샤르 필터

import cv2
import numpy as np

img = cv2.imread('DrivingRoad.jpg')

# built-in 샤르 필터
edge_gx = cv2.Scharr(img, -1, 1, 0)
edge_gy = cv2.Scharr(img, -1, 0, 1)

# 결과 출력
merged = np.hstack((img, edge_gx+edge_gy))
cv2.imshow('Scharr', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()