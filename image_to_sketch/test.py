import numpy as np
import imageio
import cv2
from scipy.ndimage import filters

def grayscale(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])

def dodge(front, back):
    result = front * 255 / (255 - back)
    result[result > 255] = 255
    result[back == 255] = 255
    return result.astype('uint8')

def create_high_pass_filter_image(input_image, output_image):
    
    img = imageio.imread(input_image)

   
    grayscale_image = grayscale(img)
    inverted_image = 255 - grayscale_image

  
    blurred_image = filters.gaussian_filter(inverted_image, sigma=10)

    final_result = dodge(blurred_image, grayscale_image)

   
    imageio.imsave(output_image, final_result)

  
    cv2.imshow('Original', img)
    cv2.imshow('Final', final_result, cmap='gray')
    cv2.waitKey(0)
    cv2.destroyAllWindows()


input_image = "elon.jpeg"
output_image = "result.jpeg"


create_high_pass_filter_image(input_image, output_image)
