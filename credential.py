# ============================================================
# credential.py
# Represents one saved account (site, username, password)
# OOP Concept: Encapsulation (private attributes + getters)
# ============================================================

class Credential:

    def __init__(self, site, username, encrypted_password):
        self.__site     = site
        self.__username = username
        self.__password = encrypted_password   # stored encrypted

    # ── Getters ─────────────────────────────────────────────
    def get_site(self):
        return self.__site

    def get_username(self):
        return self.__username

    def get_encrypted_password(self):
        return self.__password

    # ── Update password (encrypted version) ─────────────────
    def update_password(self, new_encrypted_password):
        self.__password = new_encrypted_password

    # ── Convert to dict for saving to JSON ──────────────────
    def to_dict(self):
        return {
            "site"    : self.__site,
            "username": self.__username,
            "password": self.__password
        }

    # ── Nice display format ──────────────────────────────────
    def __str__(self):
        return f"  Site     : {self.__site}\n  Username : {self.__username}"
