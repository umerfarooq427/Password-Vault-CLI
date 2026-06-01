# ============================================================
# vault.py
# Manages all credentials — save, load, search, delete
# OOP Concept: Encapsulation + Abstraction
# ============================================================

import json
import os
from credential import Credential

class Vault:

    VAULT_FILE = "vault.json"

    def __init__(self, encryptor):
        self.__encryptor   = encryptor
        self.__credentials = []
        self.__load()

    # ── Add a new credential ─────────────────────────────────
    def add(self, site, username, plain_password):
        encrypted = self.__encryptor.encrypt(plain_password)
        cred      = Credential(site, username, encrypted)
        self.__credentials.append(cred)
        self.__save()
        print(f"\n  ✅ Password saved for {site}!\n")

    # ── Retrieve a credential by site name ───────────────────
    def get(self, site):
        for cred in self.__credentials:
            if cred.get_site().lower() == site.lower():
                plain = self.__encryptor.decrypt(cred.get_encrypted_password())
                print(f"\n  ════════════════════════")
                print(cred)
                print(f"  Password : {plain}")
                print(f"  ════════════════════════\n")
                return cred
        print(f"\n  ❌ No account found for '{site}'\n")
        return None

    # ── List all saved sites ─────────────────────────────────
    def list_all(self):
        if not self.__credentials:
            print("\n  ❌ Vault is empty. No passwords saved yet.\n")
            return

        print("\n  ════════════════════════════════")
        print("        SAVED ACCOUNTS")
        print("  ════════════════════════════════")
        for i, cred in enumerate(self.__credentials, 1):
            print(f"  [{i}] {cred.get_site()}  —  {cred.get_username()}")
        print("  ════════════════════════════════\n")

    # ── Delete a credential ──────────────────────────────────
    def delete(self, site):
        for cred in self.__credentials:
            if cred.get_site().lower() == site.lower():
                self.__credentials.remove(cred)
                self.__save()
                print(f"\n  ✅ {site} deleted from vault.\n")
                return
        print(f"\n  ❌ No account found for '{site}'\n")

    # ── Update password for a site ───────────────────────────
    def update(self, site, new_plain_password):
        for cred in self.__credentials:
            if cred.get_site().lower() == site.lower():
                encrypted = self.__encryptor.encrypt(new_plain_password)
                cred.update_password(encrypted)
                self.__save()
                print(f"\n  ✅ Password updated for {site}!\n")
                return
        print(f"\n  ❌ No account found for '{site}'\n")

    # ── Return all credentials (for auditor) ─────────────────
    def get_all(self):
        return self.__credentials

    # ── Private: save vault to JSON file ────────────────────
    def __save(self):
        data = [cred.to_dict() for cred in self.__credentials]
        with open(self.VAULT_FILE, "w") as f:
            json.dump(data, f, indent=4)

    # ── Private: load vault from JSON file ──────────────────
    def __load(self):
        if os.path.exists(self.VAULT_FILE):
            with open(self.VAULT_FILE, "r") as f:
                data = json.load(f)
            for item in data:
                cred = Credential(
                    item["site"],
                    item["username"],
                    item["password"]
                )
                self.__credentials.append(cred)
