import csv
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from datetime import datetime, timedelta

def generate_certificate(common_name):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    subject = issuer = x509.Name([
        x509.NameAttribute(x509.NameOID.COMMON_NAME, common_name),
    ])

    valid_from = datetime.utcnow()
    valid_until = valid_from + timedelta(days=365)  # Valid for 1 year

    certificate = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(private_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(valid_from)
        .not_valid_after(valid_until)
        .sign(private_key, hashes.SHA256(), default_backend())
    )

    return certificate, private_key

def generate_certificates_from_csv(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header if present
        for row in reader:
            domain = row[0].strip()  # Assuming the domain is in the first column
            certificate, private_key = generate_certificate(domain)
            
            certificate_pem = certificate.public_bytes(serialization.Encoding.PEM)
            private_key_pem = private_key.private_bytes(
                serialization.Encoding.PEM,
                serialization.PrivateFormat.TraditionalOpenSSL,
                serialization.NoEncryption()
            )
            
            with open(f"{domain}_output.txt", 'w') as output_file:
                output_file.write("X.509 Certificate:\n\n")
                output_file.write(certificate_pem.decode())
                output_file.write("\n\nPrivate Key:\n\n")
                output_file.write(private_key_pem.decode())

# Example usage: Provide the path to your CSV file
csv_file_path = 'domains.csv'  # Replace with your CSV file path
generate_certificates_from_csv(csv_file_path)
