import csv
from cryptography.hazmat.primitives.asymmetric import rsa
from collections import defaultdict

# Function to generate the RSA key and return the key and its size
def generate_rsa_key():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    return private_key, private_key.key_size

def sort_keys_by_size(keys):
    return sorted(keys, key=lambda k: k[1])  # Sort the keys by their sizes

def find_identical_keys(keys):
    identical_keys = defaultdict(list)
    for index, (key, size) in enumerate(keys):
        identical_keys[key].append(index)
    return {key: indices for key, indices in identical_keys.items() if len(indices) > 1}

# Generate a list of RSA keys and their sizes
keys = [generate_rsa_key() for _ in range(10)]  # Example: Generate 10 RSA keys
keys_with_sizes = [(key[0], key[1]) for key in keys]

# Sort keys by size
sorted_keys = sort_keys_by_size(keys_with_sizes)

# Find identical keys
identical_keys = find_identical_keys(sorted_keys)

print("Sorted Keys by Size:")
for key, size in sorted_keys:
    print(f"Key Size: {size}")

print("\nIdentical Keys:")
for key, indices in identical_keys.items():
    print(f"Key: {key.public_numbers().n}, Indices: {indices}")
