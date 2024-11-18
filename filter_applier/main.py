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
    
# Write to modified_directory as we go through all the images (wihtin loop)