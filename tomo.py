import math
import matplotlib.pyplot as plt
import numpy as np
from skimage import io
from bresenham import *

# PARAMETRY:
beta = 180
d = 500
step = 2

input_image = io.imread("image.jpg")
r = min(input_image.shape[0], input_image.shape[1]) / 2 - 5

x_przes = input_image.shape[0] / 2
y_przes = input_image.shape[1] / 2

sinogram = np.ndarray(shape=(len(range(0, 360, step)), d))
output_image = np.zeros(shape=(input_image.shape[0], input_image.shape[1]))

for angle in range(0, 360, step):
    e_x = math.cos(math.radians(angle)) * r + x_przes
    e_y = math.sin(math.radians(angle)) * r + y_przes
    # print(e_x)
    # print(e_y)
    for i in range(0, d):
        alfa = math.radians(angle) + math.pi - (math.radians(beta) / 2) + (i * (math.radians(beta)) / (d - 1))
        # print(math.degrees(alfa))
        d_x = math.cos(alfa) * r + x_przes
        d_y = math.sin(alfa) * r + y_przes
        # print(d_x)
        # print(d_y)

        sinogram[angle // step][i] = bresenham(round(e_x), round(e_y), round(d_x), round(d_y), input_image, None, None)
        bresenham(round(e_x), round(e_y), round(d_x), round(d_y), input_image, sinogram[angle // step][i], output_image)


plt.imshow(output_image, cmap=plt.cm.Greys_r)
plt.show()
