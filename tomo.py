import math
import numpy as np
from bresenham import *
from sklearn import metrics


def tomograf(input_image, step, d, beta, iterations):
    r = min(input_image.shape[0], input_image.shape[1]) / 2 - 5

    x_przes = input_image.shape[0] / 2
    y_przes = input_image.shape[1] / 2

    visited = np.ones(shape=(input_image.shape[0], input_image.shape[1]))
    sinogram = np.ndarray(shape=(len(range(0, 360, step)), d))
    output_image = np.zeros(shape=(input_image.shape[0], input_image.shape[1]))

    for angle in range(0, iterations * step, step):
        e_x = math.cos(math.radians(angle)) * r + x_przes
        e_y = math.sin(math.radians(angle)) * r + y_przes
        for i in range(0, d):
            if d == 1:
                alfa = math.radians(angle) + math.pi - (math.radians(beta) / 2)
            else:
                alfa = math.radians(angle) + math.pi - (math.radians(beta) / 2) + (i * (math.radians(beta)) / (d - 1))
            d_x = math.cos(alfa) * r + x_przes
            d_y = math.sin(alfa) * r + y_przes

            sinogram[angle // step][i] = bresenham(round(e_x), round(e_y), round(d_x), round(d_y), input_image, None,
                                                   None, visited)
            bresenham(round(e_x), round(e_y), round(d_x), round(d_y), input_image, sinogram[angle // step][i],
                      output_image, None)

    output_image /= visited

    output_image_fllaten = output_image.flatten()
    output_image_list = list(set(output_image_fllaten))
    output_image_list.sort()
    output_image_list.remove(0)

    output_image[output_image == 0] = min(output_image_list)

    sinogram = ((sinogram - np.min(sinogram)) / (np.max(sinogram) - np.min(sinogram))) * 256
    output_image = ((output_image - np.min(output_image)) / (np.max(output_image) - np.min(output_image))) * 256
    mse = metrics.mean_squared_error(input_image/256,output_image/256)
    print(mse)

    # cv2.imwrite("sinogram.jpg", sinogram)
    # cv2.imwrite("output_image.jpg", output_image)

    return sinogram, output_image
