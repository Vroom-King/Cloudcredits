from cryptography.fernet import Fernet

# 🔐 Step 1: Generate and Save Key (only once)
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("✔️ Key generated and saved to secret.key")

# 🔑 Step 2: Load Existing Key
def load_key():
    try:
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("❌ Key file not found. Generate one first.")
        return None

# 🔒 Step 3: Encrypt Text
def encrypt_text(text, key):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(text.encode())
    return encrypted

# 🔓 Step 4: Decrypt Text
def decrypt_text(encrypted_text, key):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_text)
    return decrypted.decode()

# 🧠 Main Application
if __name__ == "__main__":
    print("=== AES Text Encryption Using Fernet (cryptography) ===")
    print("1. Generate Key")
    print("2. Encrypt Text")
    print("3. Decrypt Text")
    choice = input("Select an option (1/2/3): ")

    if choice == "1":
        generate_key()

    elif choice == "2":
        key = load_key()
        if key:
            text = input("Enter text to encrypt: ")
            encrypted = encrypt_text(text, key)
            print(f"\n🔐 Encrypted Text:\n{encrypted.decode()}")

    elif choice == "3":
        key = load_key()
        if key:
            encrypted_input = input("Enter encrypted text: ").encode()
            try:
                decrypted = decrypt_text(encrypted_input, key)
                print(f"\n🔓 Decrypted Text:\n{decrypted}")
            except Exception as e:
                print("❌ Decryption failed:", e)
    else:
        print("❌ Invalid option.")

