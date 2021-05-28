# 라플라시안 마스크 필터

import cv2
import numpy as np

img = cv2.imread('DrivingRoad.jpg')

# 라플라시안 필터
edge = cv2.Laplacian(img, -1)

# 결과 출력
merged = np.hstack((img, edge))
cv2.imshow('Laplacian', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()