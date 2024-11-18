import cv2
import numpy as np
import sys

#Type in image name
imgname = input("Image name (e.g. image.jpg): ")

#Read image
img = cv2.imread(imgname)

if img is None :
    print ("Error opening image")
    sys.exit(-1)

# Split image into RGB channels
b,g,r = cv2.split(img)

# Shift the red and blue channels
blue_shift_amount = input("Blue shift amount:")
red_shift_amount = input("Red shift amount:")
blue_shifted = np.roll(b, blue_shift_amount, axis = 1)
red_shifted = np.roll(r, red_shift_amount, axis = 1)

# Merge shifted channels back
output_image = cv2.merge((blue_shifted, g, red_shifted))

# Save the altered image
cv2.imwrite("newimgpy.jpg", output_image)
cv2.imshow("Chromatic Aberration", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()