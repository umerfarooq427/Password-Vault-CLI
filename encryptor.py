# ============================================================
# encryptor.py
# Handles encrypting and decrypting passwords using Fernet
# OOP Concept: Encapsulation (hides encryption logic)
# ============================================================

from cryptography.fernet import Fernet
import os

class Encryptor:

    KEY_FILE = "secret.key"

    def __init__(self):
        self.__key  = self.__load_or_create_key()
        self.__fernet = Fernet(self.__key)

    # ── Private: load key from file or create new one ──────
    def __load_or_create_key(self):
        if os.path.exists(self.KEY_FILE):
            with open(self.KEY_FILE, "rb") as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(self.KEY_FILE, "wb") as f:
                f.write(key)
            return key

    # ── Public: encrypt a plain text password ──────────────
    def encrypt(self, plain_text):
        return self.__fernet.encrypt(plain_text.encode()).decode()

    # ── Public: decrypt an encrypted password ──────────────
    def decrypt(self, encrypted_text):
        return self.__fernet.decrypt(encrypted_text.encode()).decode()
