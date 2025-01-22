from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from datetime import datetime, timedelta

def generate_certificate(common_name):
    # Generate a private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    # Specify the details for the certificate
    subject = issuer = x509.Name([
        x509.NameAttribute(x509.NameOID.COMMON_NAME, common_name),
    ])

    valid_from = datetime.utcnow()
    valid_until = valid_from + timedelta(days=365)  # Valid for 1 year

    # Create the certificate
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

# Example usage
common_name = "google.com"
certificate, private_key = generate_certificate(common_name)

# Serialize the certificate and private key
certificate_pem = certificate.public_bytes(serialization.Encoding.PEM)
private_key_pem = private_key.private_bytes(
    serialization.Encoding.PEM,
    serialization.PrivateFormat.TraditionalOpenSSL,
    serialization.NoEncryption()
)

# Print or use the certificate and private key as needed
print("X.509 Certificate:\n", certificate_pem.decode())
print("\nPrivate Key:\n", private_key_pem.decode())
