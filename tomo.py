import math
import numpy as np
import cv2
from bresenham import *


def tomograf(input_image, step, d, beta, iterations):
    r = min(input_image.shape[0], input_image.shape[1]) / 2 - 5

    x_przes = input_image.shape[0] / 2
    y_przes = input_image.shape[1] / 2

    sinogram = np.ndarray(shape=(len(range(0, 360, step)), d))
    output_image = np.zeros(shape=(input_image.shape[0], input_image.shape[1]))

    for angle in range(0, iterations * step, step):
        e_x = math.cos(math.radians(angle)) * r + x_przes
        e_y = math.sin(math.radians(angle)) * r + y_przes
        for i in range(0, d):
            alfa = math.radians(angle) + math.pi - (math.radians(beta) / 2) + (i * (math.radians(beta)) / (d - 1))
            d_x = math.cos(alfa) * r + x_przes
            d_y = math.sin(alfa) * r + y_przes

            sinogram[angle // step][i] = bresenham(round(e_x), round(e_y), round(d_x), round(d_y), input_image, None,
                                                   None)
            bresenham(round(e_x), round(e_y), round(d_x), round(d_y), input_image, sinogram[angle // step][i],
                      output_image)

    sinogram = ((sinogram - np.min(sinogram)) / (np.max(sinogram) - np.min(sinogram))) * 256
    output_image = ((output_image - np.min(output_image)) / (np.max(output_image) - np.min(output_image))) * 256

    # cv2.imwrite("sinogram.jpg", sinogram)
    # cv2.imwrite("output_image.jpg", output_image)

    return sinogram, output_image
