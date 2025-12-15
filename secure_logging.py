# secure_logging.py

import os
import json
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding


# ---------- KEY HELPERS ----------

def load_public_key(path="public_key.pem"):
    with open(path, "rb") as f:
        return serialization.load_pem_public_key(f.read())


def load_private_key(path="private_key.pem"):
    with open(path, "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None)


def _b64(x: bytes) -> str:
    return base64.b64encode(x).decode()


def _b64d(s: str) -> bytes:
    return base64.b64decode(s)


# ---------- ENCRYPTION ----------

def encrypt_log(message: str, out_file="secure_log.json"):
    public_key = load_public_key()

    # AES-256 key + nonce
    aes_key = os.urandom(32)
    nonce = os.urandom(12)
    aesgcm = AESGCM(aes_key)

    # Encrypt message
    ciphertext = aesgcm.encrypt(nonce, message.encode(), None)

    # Encrypt AES key using RSA-OAEP
    encrypted_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Save encrypted package
    package = {
        "encrypted_key": _b64(encrypted_key),
        "nonce": _b64(nonce),
        "ciphertext": _b64(ciphertext)
    }

    with open(out_file, "w") as f:
        json.dump(package, f, indent=2)

    return out_file


# ---------- DECRYPTION ----------

def decrypt_log(in_file="secure_log.json"):
    private_key = load_private_key()

    with open(in_file, "r") as f:
        package = json.load(f)

    encrypted_key = _b64d(package["encrypted_key"])
    nonce = _b64d(package["nonce"])
    ciphertext = _b64d(package["ciphertext"])

    # Recover AES key
    aes_key = private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    aesgcm = AESGCM(aes_key)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)

    return plaintext.decode()
