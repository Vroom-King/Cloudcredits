# 🖼️ Image Encryption Using Cryptographic Algorithms (AES)

This project implements a secure method for encrypting and decrypting image files using **AES (Advanced Encryption Standard)** in Python. It demonstrates how sensitive image data can be protected from unauthorized access using modern cryptographic techniques.

---

## 🔐 Features

- 📸 Encrypt and decrypt `.png`, `.jpg`, or `.bmp` image files
- 🔑 AES-256 symmetric key encryption
- ✅ Ensures confidentiality and preserves image data integrity
- 🧩 Supports byte-level image manipulation
- 💻 CLI-based Python tool

---

## 📌 Objective

To develop a basic, yet secure image encryption system using AES encryption and decryption techniques for protecting image files from unauthorized access.

---

## 🧰 Technologies Used

- Python 3
- [`cryptography`](https://cryptography.io/en/latest/) (Fernet or AES modes)
- `Pillow` for optional image format handling
- `os` and `base64` for file management

---

## 🧪 Sample Usage

```bash
$ python Image-Encryption.py encrypt input.jpg
🔐 Encrypted file saved as: encrypted_image.enc

$ python Image-Encryption.py decrypt encrypted.img 
🔓 Decrypted image saved as: output.jpg
```

Installation
```bash
git clone https://github.com/Vroom-King/Cloudcredits.git
cd Cloudcredits
cd Image-Encryption
```

Install the dependencies:
```bash
pip install cryptography pillow
```

How It Works

    Read image as binary data

    Generate or load a symmetric AES key

    Encrypt or decrypt the image using AES-CBC or Fernet (AES-CBC + HMAC)

    Save encrypted data as a binary file or restore to image format
