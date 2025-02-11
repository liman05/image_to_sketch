import numpy as np
import imageio
import cv2
from scipy.ndimage import filters

img = "elon.jpeg"

def grayscale(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])

def dodge(front, back):
    result = front * 255 / (255 - back)
    result[result > 255] = 255
    result[back == 255] = 255
    return result.astype('uint8')

s = imageio.imread(img)
g = grayscale(s)
i = 255 - g

b = filters.gaussian_filter(i, sigma=10)
r = dodge(b, g)

cv2.imshow('Original', s)
cv2.imshow('Grayscale', g, cmap='gray')
cv2.imshow('Inverted', i, cmap='gray')
cv2.imshow('Blurred', b, cmap='gray')
cv2.imshow('Final', r, cmap='gray')

cv2.waitKey(0)
cv2.destroyAllWindows()
#
