from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256
import struct

def derive_key(secret: bytes) -> bytes:
    return SHA256.new(secret).digest()  # 256-bit key

def encrypt_cc(card_str: str, key: bytes) -> bytes:
    assert len(card_str) == 16 and card_str.isdigit()
    card_int = int(card_str)
    pt = struct.pack('>Q', card_int)  # pack 64-bit integer to bytes
    nonce = get_random_bytes(12)  # GCM standard nonce size

    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    ct, tag = cipher.encrypt_and_digest(pt)
    return nonce + ct + tag  # full encrypted blob

def decrypt_cc(encrypted: bytes, key: bytes) -> str:
    nonce = encrypted[:12]
    ct = encrypted[12:-16]
    tag = encrypted[-16:]

    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    pt = cipher.decrypt_and_verify(ct, tag)
    return str(struct.unpack('>Q', pt)[0]).zfill(16)

if __name__ == "__main__":
    secret = b"your-secure-password"  # use an environment variable in real apps
    key = derive_key(secret)

    card = input("Enter a 16-digit credit card number: ").strip()
    encrypted = encrypt_cc(card, key)
    print("🔐 Encrypted (hex):", encrypted.hex())

    decrypted = decrypt_cc(encrypted, key)
    print("🔓 Decrypted:", decrypted)

    print("✅ Match" if decrypted == card else "❌ Mismatch")

