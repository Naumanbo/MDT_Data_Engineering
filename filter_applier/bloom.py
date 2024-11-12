import os
import sys
import pickle
from bloom_filter2 import BloomFilter

def create_bloom_filter(filename):
    # Construct the output filename
    base_name = os.path.splitext(filename)[0]
    output_filename = f"{base_name}_copyBLOOM"

    # Initialize Bloom filter parameters
    expected_items = 10000           # Adjust based on your dataset size
    false_positive_rate = 0.01       # Adjust based on acceptable false positive rate

    # Create a Bloom filter
    bloom = BloomFilter(max_elements=expected_items, error_rate=false_positive_rate)

    # Read data from the input file and add to the Bloom filter
    with open(filename, 'r') as infile:
        for line in infile:
            item = line.strip()
            bloom.add(item)

    # Serialize and save the Bloom filter to the output file
    with open(output_filename, 'wb') as outfile:
        pickle.dump(bloom, outfile)

    print(f"Bloom filter created and saved to {output_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python bloom_filter.py <input_filename>")
        sys.exit(1)

    input_file = sys.argv[1]
    create_bloom_filter(input_file)
