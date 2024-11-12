from PIL import Image, ImageFilter, ImageEnhance
import sys
import os

def apply_bloom_filter(filename):
    # Construct the output filename
    base_name = os.path.splitext(filename)[0]
    output_filename = f"{base_name}_bloom.jpg"

    # Open the original image
    with Image.open(filename) as img:
        # Step 1: Create a blurred version of the image to simulate bloom
        blurred_img = img.filter(ImageFilter.GaussianBlur(radius=10))  # Adjust radius for more or less bloom

        # Step 2: Enhance brightness of the blurred image
        enhancer = ImageEnhance.Brightness(blurred_img)
        bright_blurred_img = enhancer.enhance(1.5)  # Adjust this value to control bloom intensity

        # Step 3: Combine the original and bright blurred images
        bloom_img = Image.blend(img, bright_blurred_img, alpha=0.5)  # Adjust alpha for more or less bloom

        # Save the final image with the bloom effect
        bloom_img.save(output_filename, "JPEG")

    print(f"Bloom filter applied and saved to {output_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python bloom_filter.py <input_filename>")
        sys.exit(1)

    input_file = sys.argv[1]
    apply_bloom_filter(input_file)
