# 로버츠 교차 필터

import cv2
import numpy as np

img = cv2.imread('IMAGE1.jpg')
img = cv2.pyrDown(img)
img = cv2.pyrDown(img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 로버츠 커널 생성
gx_kernel = np.array([[1,0], [0,-1]])
gy_kernel = np.array([[0, 1],[-1,0]])

# 커널 적용
edge_gx = cv2.filter2D(gray, -1, gx_kernel)
edge_gy = cv2.filter2D(gray, -1, gy_kernel)
merged = edge_gx + edge_gy

# 결과 출력
#merged = np.hstack((img, edge_gx+edge_gy))
cv2.imshow('Original', img)
cv2.imshow('Roberts', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()