# Import
import os
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Data
filepath = "data/"
files = os.listdir(filepath)
images = {}
# Loading Files
print("Loading files from " + filepath)
for file in files:
    print("# " + file)
    images[file] = Image.open(filepath + file, 'r')
    plt.imshow(images[file])
    plt.title(file)
    plt.show()

# Load GTA Picture
image = images['image.png']




plt.imshow(image)
plt.show()