""" After applying filters, assess if accuracy of human detection in modified dataset
is higher than original dataset on a custom test set designed to include
images with real artifacts

Potential ways to create test set:
1. Get 50% of images from original test set and seed images of real artifacts from other datasets
for the rest.
   a. This way, bias is reduced since 50% of test set are images that the model was not trained to detect
   b. Want to verify that our modified dataset has a higher accuracy score in detecting humans in worse camera conditions

Requirements:
1. Train two seperate ML models:
   a. Model 1: trained on original dataset
   b. Model 2: trained on modified dataset
2. Feed both models the custom test set
3. Create an answer sheet .csv file for each model
4. Compare each models answer to answer key and return each models accuracy on test set
"""
