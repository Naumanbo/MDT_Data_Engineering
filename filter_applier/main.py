"""
This program parses through a directory of all images in training set and applies 1 of 4
filters to them. Then, it creates a new training set based on the modified images. Lastly, 
this modified dataset will be used to train a ML model and compare accuracy against original model.


Example directory:
-images
|
 -drone-000
  |
   -img1.png   
   -img2.png
   ...
 -drone-001
  |
   -img1.png   
   -img2.png
   ...
  
         
Constraints:
1. A maximum of 20% of images from the dataset can be modified
2. Images that are modified must overwrite the original file to keep data consistent with
the labels data
3. Throw an exception if a image file does not open or directory does not exist

Requirements:
1. Stores a copy of original training set and test set to compare accuracy later on
2. Need a way to test original data set with modified one without bias (can't use same filters on test set because modified one will obviously score higher)
"""

import time
import sys
import random

# Fetch the time
seconds = time.time()

# Set random seed using time

# drone_pics folder

#Check if exist
if drone_pics is None :
    print ("Error opening image")
    sys.exit(-1)


# For each image in the dataset, choose which ones to modify and apply filters
# Generate numbers 1-100, if numbers 1-20, modify the image
random_num = random.randint(1,100)
if random_num <= 20 :
    #Modify
# Generate numbers 1-4 to choose which filter to apply/Randomly determine the order
# of the filters and apply them repeatedly in that order.
# Code: 1: Bloom. 2: Blur. 3: Chromatic Aberration. 4: Film Grain.
    
# Write to modified_directory as we go through all the images (within loop)