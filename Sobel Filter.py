# 소벨 필터

import cv2
import numpy as np

img = cv2.imread('DrivingRoad.jpg')

# 소벨 커널 생성
gx_k = np.array([[-1,0,1], [-2,0,2],[-1,0,1]])
gy_k = np.array([[-1,-2,-1],[0,0,0], [1,2,1]])

# 커널 필터 적용
edge_gx = cv2.filter2D(img, -1, gx_k)
edge_gy = cv2.filter2D(img, -1, gy_k)

# 결과 출력
merged = np.hstack((img, edge_gx+edge_gy))
cv2.imshow('sobel', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()