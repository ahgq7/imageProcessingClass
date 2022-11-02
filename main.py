import cv2
from matplotlib import pyplot as plt
import matplotlib
from numpy import zeros, shape

foto = cv2.imread("ornek.webp")
B = foto[:,:,0]
G = foto[:,:,1]
R = foto[:,:,2]

matplotlib.use('TkAgg')
imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B

histogram = zeros(256)
[w,h] = shape(imgGray)
for v in range(0, h):
    for u in range(0, w):
        i = imgGray[u,v]
        j = int(i)
        histogram[j] = histogram[j]+1

plt.figure(1)
plt.plot(histogram)
plt.show()