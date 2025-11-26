
import pyotp, qrcode

def generate_totp_secret():
    return pyotp.random_base32()

def get_qr_code(secret, username):
    uri = pyotp.totp.TOTP(secret).provisioning_uri(name=username, issuer_name="SecureApp")
    img = qrcode.make(uri)
    img.save(f"{username}_qrcode.png")
    print(f"QR code saved as {username}_qrcode.png")

def verify_totp(token, secret):
    return pyotp.TOTP(secret).verify(token)
