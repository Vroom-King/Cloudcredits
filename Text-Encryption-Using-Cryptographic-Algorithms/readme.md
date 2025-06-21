# 🔐 Text Encryption Using Cryptographic Algorithms (AES-Fernet)

This project implements a secure and reversible encryption-decryption system for text messages using the **Fernet implementation of AES (AES-128-CBC + HMAC)** provided by Python’s `cryptography` library. It's ideal for securely storing or transmitting sensitive strings.

---

## 📌 Features

- 🔑 AES-based encryption using Fernet
- ✅ Authenticated encryption (confidentiality + integrity)
- 📥 Encrypt plain text messages
- 📤 Decrypt messages with a secret key
- 💻 Command-line interface (CLI)

---

## 💡 How It Works

1. A key is generated using `Fernet.generate_key()`.
2. Input text is encrypted and encoded using that key.
3. The ciphertext can be securely stored or transmitted.
4. Only the original key can decrypt the ciphertext back to plain text.

---

## 🧰 Technologies Used

- Python 3
- [`cryptography`](https://cryptography.io/en/latest/) library
- Fernet (AES-128 in CBC mode + HMAC + Base64 encoding)

---

## 🧪 Sample Output

```bash
$ python text_encryption.py
Enter the message to encrypt: Hello, World!
🔐 Encrypted: gAAAAABl...
🔓 Decrypted: Hello, World!
```

Clone this repository:
```bash
git clone https://github.com/your-username/Text-Encryption-Using-Cryptographic-Algorithms.git
cd Text-Encryption-Using-Cryptographic-Algorithms
```
Install the required library:
```bash
pip install cryptography
```

Usage

```bash
python text_encryption.py
```
You will be prompted to:

    Generate secret key

    Run script again
    
    Enter a message

    View the encrypted result

    See the decrypted message using the same key
