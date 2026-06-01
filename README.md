# 🔐 Password Vault CLI

A command-line password manager built with Python using Object-Oriented Programming (OOP) principles. This project was made as part of a 2nd semester OOP course and is related to **cybersecurity**.

---

## 📌 What it does

- 💾 Save passwords for any account (encrypted)
- 🔍 Retrieve saved passwords instantly
- 📋 List all saved accounts
- ✏️ Update existing passwords
- 🗑️ Delete accounts from vault
- ⚡ Generate strong random passwords
- 🛡️ Audit all passwords for weaknesses and reuse

---

## 🏗️ OOP Concepts Used

| Concept | Where it's applied |
|---|---|
| **Classes & Objects** | Each component is its own class |
| **Encapsulation** | Private `__attributes` in Credential and Encryptor |
| **Abstraction** | User calls `vault.add()` without knowing encryption logic |
| **Inheritance** | Custom exceptions extend base Exception class |

---

## 📁 Project Structure

```
password-vault-cli/
 ├── main.py                ← entry point, run this
 ├── vault.py               ← manages all credentials
 ├── credential.py          ← represents one account
 ├── encryptor.py           ← encrypts and decrypts passwords
 ├── password_auditor.py    ← checks password strength and reuse
 └── password_generator.py  ← generates strong passwords
```

---

## ⚙️ Requirements

- Python 3.x
- cryptography library

---

## 🚀 How to Run

**Step 1 — Install the required library**
```
pip install cryptography
```

**Step 2 — Run the app**
```
python main.py
```

---

## 🖥️ Menu Options

```
╔══════════════════════════════════════╗
║       🔐 PASSWORD VAULT CLI         ║
╠══════════════════════════════════════╣
║  [1]  Save a password               ║
║  [2]  Get a password                ║
║  [3]  List all accounts             ║
║  [4]  Update a password             ║
║  [5]  Delete an account             ║
║  [6]  Generate strong password      ║
║  [7]  Audit all passwords           ║
║  [8]  Exit                          ║
╚══════════════════════════════════════╝
```

---

## 🔒 How Encryption Works

- Passwords are encrypted using **Fernet symmetric encryption** from the `cryptography` library
- A secret key is automatically generated and saved in `secret.key`
- Passwords are **never stored as plain text** — only encrypted versions are saved in `vault.json`
- The key is required to decrypt — without it passwords cannot be read

---

## 🛡️ Password Strength Rules

A password is considered **STRONG** if it has:
- At least 8 characters
- At least one uppercase letter (A-Z)
- At least one lowercase letter (a-z)
- At least one number (0-9)
- At least one special character (!@#$%^&*)

---

## ⚠️ Important

- Do **NOT** delete or share `secret.key` — it is needed to decrypt your passwords
- Do **NOT** upload `secret.key` or `vault.json` to GitHub
- This project is for educational purposes only

---

## 👥 Team Members

| Name | File Responsible |
|---|---|
| Umer farooq | main.py |
| Ayan hassan | vault.py |
| Matti Ullah| credential.py + encryptor.py |
| Ather ahmed + Muhammad hannan | password_auditor.py + password_generator.py |

---

## 📚 Course Info

- **Subject** : Object Oriented Programming (OOP)
- **Language** : Python 3
- **Semester** : 2nd Semester
