import os
import random
from PIL import Image, ImageFilter

def get_image_files(directory):

    image_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(('.png', '.jpg', '.jpeg'))]
    return image_files

def pick_random_subset(image_files, percentage=20):

    subset_size = int(len(image_files) * (percentage / 100))
    return random.sample(image_files, subset_size)

def apply_blur_filter(image_file, output_directory):

    img = Image.open(image_file)

    blurred_img = img.filter(ImageFilter.BLUR)

    output_path = os.path.join(output_directory, os.path.basename(image_file))
    blurred_img.save(output_path)
    print(f"Blurred image saved to {output_path}")

def main(input_directory, output_directory):

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    image_files = get_image_files(input_directory)

    selected_files = pick_random_subset(image_files)

    for image_file in selected_files:
        apply_blur_filter(image_file, output_directory)

if __name__ == '__main__':

    input_dir = '/Users/chaminsuh/Documents/drone_005'
    output_dir = '/Users/chaminsuh/Documents/filtered2'
    
    main(input_dir, output_dir)
