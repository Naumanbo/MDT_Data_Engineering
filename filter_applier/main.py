"""
This program parses through a directory of all images in training set and applies 1 of 4
filters to them
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
