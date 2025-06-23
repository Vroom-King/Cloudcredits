# 🔐 Credit Card Encryption & Decryption Using AES-GCM

This project demonstrates how to securely encrypt and decrypt credit card numbers using **AES-GCM** in Python. AES-GCM (Galois/Counter Mode) provides both **confidentiality and integrity**, making it ideal for protecting sensitive data such as credit card information.

---

## 📌 Features

- ✅ AES-256 encryption using GCM mode
- 🔑 Key derivation using SHA-256
- 🛡️ Authentication tag verification
- 🧪 Reversible encryption-decryption cycle
- 💡 Educational, CLI-based implementation

---

## 🧰 Technologies Used

- Python 3
- [PyCryptodome](https://www.pycryptodome.org/) – cryptographic library
- AES (Advanced Encryption Standard) – symmetric encryption
- GCM – authenticated encryption mode
- SHA-256 – for secure key derivation

---

## 🚀 How It Works

1. User enters a **16-digit credit card number**.
2. The card number is packed into 64-bit bytes.
3. A **secure AES key** is derived using SHA-256.
4. The number is encrypted using **AES-GCM** with a unique nonce.
5. Decryption requires the **same key, nonce, and authentication tag**.

---

## 🧪 Sample Usage

```bash
$ python credit_card_encrypt.py
Enter a 16-digit credit card number: 0123456789101112
🔐 Encrypted (hex): 8f2d3a...
🔓 Decrypted: 0123456789101112
✅ Match
```

Setup Instructions
```bash
git clone https://github.com/Vroom-King/Cloudcredits.git
cd Cloudcredits
cd credit-card-encryption-aes
```
Install dependencies:
```bash
pip install pycryptodome
```

Run the script:

```bash
python credit_card_encrypt.py
```

This project is for educational purposes only and does not comply with PCI-DSS or production-grade security practices.
For secure real-world applications, use certified libraries, secure key vaults, and compliance-tested storage methods.
