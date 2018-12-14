# Import
import os
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import YCbCr

# Data
filepath = "data/"
image = Image.open(filepath + 'image.png', 'r')
plt.imshow(image)
plt.show()

# BitShift
plt.subplot(3, 3, 1)
plt.imshow(image)
plt.title("Original")
image_bitshifted = []
for i in range(1, 9):
    temp = np.asarray(image)
    temp = temp >> i
    temp = temp << i
    image_bitshifted.append(temp)
    plt.subplot(3, 3, i + 1)
    plt.imshow(temp)
    plt.title("Bits Sheared by " + str(i))
plt.show()

# YCbCr

image_YCbCr = YCbCr.showYCbCr(image)
