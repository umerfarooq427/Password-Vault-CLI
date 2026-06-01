# ============================================================
# main.py
# VaultApp — main controller, runs the CLI menu
# OOP Concept: Abstraction (ties all classes together)
# ============================================================

from encryptor        import Encryptor
from vault            import Vault
from password_auditor import PasswordAuditor
from password_generator import PasswordGenerator

class VaultApp:

    def __init__(self):
        self.__encryptor  = Encryptor()
        self.__vault      = Vault(self.__encryptor)
        self.__auditor    = PasswordAuditor()
        self.__generator  = PasswordGenerator()

    # ── Display the main menu ────────────────────────────────
    def __show_menu(self):
        print("  ╔══════════════════════════════════╗")
        print("  ║       🔐 PASSWORD VAULT CLI      ║")
        print("  ╠══════════════════════════════════╣")
        print("  ║  [1]  Save a password            ║")
        print("  ║  [2]  Get a password             ║")
        print("  ║  [3]  List all accounts          ║")
        print("  ║  [4]  Update a password          ║")
        print("  ║  [5]  Delete an account          ║")
        print("  ║  [6]  Generate strong password   ║")
        print("  ║  [7]  Audit all passwords        ║")
        print("  ║  [8]  Exit                       ║")
        print("  ╚══════════════════════════════════╝")

    # ── Handle Save ─────────────────────────────────────────
    def __handle_save(self):
        print("\n  ── Save Password ──")
        site     = input("  Site name   : ").strip()
        username = input("  Username    : ").strip()
        password = input("  Password    : ").strip()

        if not site or not username or not password:
            print("\n  ❌ All fields are required.\n")
            return

        # Warn if password is weak before saving
        status, issues = self.__auditor.check_strength(password)
        if status == "WEAK":
            print("\n  ⚠️  Warning: Your password is WEAK!")
            for issue in issues:
                print(f"     → {issue}")
            choice = input("\n  Save anyway? (y/n): ").strip().lower()
            if choice != "y":
                print("  Cancelled.\n")
                return

        self.__vault.add(site, username, password)

    # ── Handle Get ──────────────────────────────────────────
    def __handle_get(self):
        print("\n  ── Get Password ──")
        site = input("  Enter site name: ").strip()
        self.__vault.get(site)

    # ── Handle Update ───────────────────────────────────────
    def __handle_update(self):
        print("\n  ── Update Password ──")
        site     = input("  Enter site name   : ").strip()
        new_pass = input("  Enter new password: ").strip()

        status, issues = self.__auditor.check_strength(new_pass)
        if status == "WEAK":
            print("\n  ⚠️  Warning: New password is WEAK!")
            for issue in issues:
                print(f"     → {issue}")
            choice = input("\n  Update anyway? (y/n): ").strip().lower()
            if choice != "y":
                print("  Cancelled.\n")
                return

        self.__vault.update(site, new_pass)

    # ── Handle Delete ───────────────────────────────────────
    def __handle_delete(self):
        print("\n  ── Delete Account ──")
        site = input("  Enter site name: ").strip()
        confirm = input(f"  Are you sure you want to delete '{site}'? (y/n): ").strip().lower()
        if confirm == "y":
            self.__vault.delete(site)
        else:
            print("  Cancelled.\n")

    # ── Handle Generate ─────────────────────────────────────
    def __handle_generate(self):
        print("\n  ── Generate Strong Password ──")
        try:
            length = int(input("  Enter length (default 12): ").strip() or "12")
            self.__generator.set_length(length)
        except ValueError:
            length = 12

        password = self.__generator.generate()
        print(f"\n  ✅ Generated Password: {password}\n")

        save = input("  Do you want to save this password? (y/n): ").strip().lower()
        if save == "y":
            site     = input("  Site name : ").strip()
            username = input("  Username  : ").strip()
            self.__vault.add(site, username, password)

    # ── Handle Audit ────────────────────────────────────────
    def __handle_audit(self):
        all_creds = self.__vault.get_all()
        if not all_creds:
            print("\n  ❌ No passwords to audit.\n")
            return
        self.__auditor.audit_all(all_creds, self.__encryptor)

    # ── Main run loop ────────────────────────────────────────
    def run(self):
        print("\n  Welcome to Password Vault CLI 🔐\n")

        while True:
            self.__show_menu()
            choice = input("\n  Enter choice (1-8): ").strip()

            if   choice == "1": self.__handle_save()
            elif choice == "2": self.__handle_get()
            elif choice == "3": self.__vault.list_all()
            elif choice == "4": self.__handle_update()
            elif choice == "5": self.__handle_delete()
            elif choice == "6": self.__handle_generate()
            elif choice == "7": self.__handle_audit()
            elif choice == "8":
                print("\n  Goodbye! Stay safe 🔐\n")
                break
            else:
                print("\n  ❌ Invalid choice. Enter 1-8.\n")


# ── Entry point ──────────────────────────────────────────────
if __name__ == "__main__":
    app = VaultApp()
    app.run()
