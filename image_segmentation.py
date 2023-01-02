from skimage import data
from skimage.io import imread, imshow
from skimage.filters import threshold_isodata
from matplotlib import pyplot as plt
import numpy as np


# Import image
img = imread('Phase_A1_1_00d00h00m.tif', as_gray = True)

# Threshold
thresh_min = threshold_isodata(img)
binary_min = img > thresh_min

fig, ax = plt.subplots(1, 2, figsize = (15, 15))


ax[0].imshow(image, cmap = plt.cm.gray)
ax[0].set_title('Original')

ax[1].imshow(binary_min, cmap = plt.cm.gray)
ax[1].set_title('Isodata')

for a in ax[:0]:
    a.axis('off')
    plt.show()

