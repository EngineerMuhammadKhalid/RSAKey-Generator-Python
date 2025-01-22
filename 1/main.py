import time
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import json
from math import gcd
from functools import reduce

def generate_rsa_keys(num_keys):
    keys = []
    start_time = time.time()

    for _ in range(num_keys):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        public_key = private_key.public_key()

        # Get the modulus in hexadecimal format
        modulus = private_key.public_key().public_numbers().n
        modulus_hex = hex(modulus)[2:]

        keys.append({
            'public_key': public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ).decode('utf-8'),
            'private_key': private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ).decode('utf-8'),
            'modulus': modulus_hex
        })

    end_time = time.time()
    print(f"Time taken to generate {num_keys} RSA keys: {end_time - start_time} seconds")

    return keys

def sort_and_find_identical(keys):
    # Sort the keys by modulus
    sorted_keys = sorted(keys, key=lambda x: x['modulus'])

    # Find identical keys based on modulus
    identical_keys = []
    seen_moduli = set()

    for key in sorted_keys:
        modulus = key['modulus']

        if modulus not in seen_moduli:
            seen_moduli.add(modulus)
        else:
            identical_keys.append(key)

    return sorted_keys, identical_keys

def batch_gcd(keys):
    moduli = [int(key['modulus'], 16) for key in keys]

    if not moduli:
        return None  # No common factor if there are no keys

    g = reduce(gcd, moduli)
    return g

def save_to_json(keys, filename):
    with open(filename, 'w') as json_file:
        json.dump(keys, json_file, indent=4)

def main():
    num_keys_to_generate = 100  # Adjust as needed
    generated_keys = generate_rsa_keys(num_keys_to_generate)

    sorted_keys, identical_keys = sort_and_find_identical(generated_keys)

    save_to_json(sorted_keys, 'sorted_rsa_keys.json')
    save_to_json(identical_keys, 'identical_rsa_keys.json')

    if identical_keys:
        common_factor = batch_gcd(identical_keys)
        if common_factor is not None:
            print(f"Common prime factor: {common_factor}")
        else:
            print("No common prime factor found.")
    else:
        print("No identical keys found.")

if __name__ == "__main__":
    main()
