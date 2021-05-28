# 샤르 필터

import cv2
import numpy as np

img = cv2.imread('DrivingRoad.jpg')

# 샤르 커널 생성
gx_k = np.array([[-3,0,3], [-10,0,10],[-3,0,3]])
gy_k = np.array([[-3,-10,-3],[0,0,0], [3,10,3]])

# 커널 필터 적용
edge_gx = cv2.filter2D(img, -1, gx_k)
edge_gy = cv2.filter2D(img, -1, gy_k)

# 결과 출력
merged = np.hstack((img, edge_gx+edge_gy))
cv2.imshow('Scharr', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()