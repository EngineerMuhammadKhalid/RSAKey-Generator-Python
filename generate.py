import time
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import json

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

        # Get the public key in PEM format
        pem_public_key = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        # Get the private key in PEM format (this is for testing purposes only)
        pem_private_key = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        keys.append({
            'public_key': pem_public_key.decode('utf-8'),
            'private_key': pem_private_key.decode('utf-8')
        })

    end_time = time.time()
    print(f"Time taken to generate {num_keys} RSA keys: {end_time - start_time} seconds")

    return keys

def save_to_json(keys):
    with open('rsa_keys.json', 'w') as json_file:
        json.dump(keys, json_file, indent=4)

if __name__ == "__main__":
    num_keys_to_generate = 10  # Adjust as needed
    generated_keys = generate_rsa_keys(num_keys_to_generate)
    save_to_json(generated_keys)
