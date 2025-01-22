from math import gcd
from functools import reduce

def batch_gcd(keys):
    moduli = [int(key['modulus'], 16) for key in keys]
    g = reduce(gcd, moduli)
    return g

def main():
    num_keys_to_generate = 10  # Adjust as needed
    generated_keys = generate_rsa_keys(num_keys_to_generate)

    sorted_keys, identical_keys = sort_and_find_identical(generated_keys)

    save_to_json(sorted_keys, 'sorted_rsa_keys.json')
    save_to_json(identical_keys, 'identical_rsa_keys.json')

    common_factor = batch_gcd(identical_keys)
    print(f"Common prime factor: {common_factor}")

if __name__ == "__main__":
    main()
