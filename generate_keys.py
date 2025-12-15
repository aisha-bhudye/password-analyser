#!/usr/bin/env python3
"""
Generate RSA keypair for hybrid encryption.
Creates:
- private_key.pem
- public_key.pem
"""

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def main():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    with open("private_key.pem", "wb") as f:
        f.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
        )

    public_key = private_key.public_key()
    with open("public_key.pem", "wb") as f:
        f.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )

    print(" Keys generated: private_key.pem, public_key.pem")


if __name__ == "__main__":
    main()
