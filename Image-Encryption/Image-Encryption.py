from cryptography.fernet import Fernet
import sys
import os

# ---------- Step 1: Generate a Key ----------
def generate_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        print("Key generated and saved as 'secret.key'")
    else:
        print("Key already exists. Skipping generation.")

# ---------- Step 2: Load the Key ----------
def load_key():
    return open("secret.key", "rb").read()

# ---------- Step 3: Encrypt Image ----------
def encrypt_image(image_path, output_path):
    key = load_key()
    f = Fernet(key)

    with open(image_path, "rb") as file:
        image_data = file.read()

    encrypted_data = f.encrypt(image_data)

    with open(output_path, "wb") as file:
        file.write(encrypted_data)

    print("Image encrypted and saved as '{}'".format(output_path))

# ---------- Step 4: Decrypt Image ----------
def decrypt_image(encrypted_path, output_path):
    key = load_key()
    f = Fernet(key)

    with open(encrypted_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(output_path, "wb") as file:
        file.write(decrypted_data)

    print("Image decrypted and saved as '{}'".format(output_path))


# ---------- Example Usage ----------
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python test.py encrypt <image_path>")
        print("  python test.py decrypt <encrypted_file_path>")
        sys.exit(1)

    mode = sys.argv[1].lower()
    path = sys.argv[2]

    generate_key()

    if mode == "encrypt":
        encrypt_image(path, "encrypted_image.enc")
    elif mode == "decrypt":
        decrypt_image(path, "decrypted_image.jpg")
    else:
        print("Unknown mode. Use 'encrypt' or 'decrypt'.")
