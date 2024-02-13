import numpy as np

pts = np.array([[100,120],[110,130],[130,150],[150,170]])

print(pts.shape)

print(pts)

print()

pts.reshape((-1,1,2))

print(pts)