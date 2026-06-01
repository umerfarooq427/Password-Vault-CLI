# ============================================================
# password_auditor.py
# Checks if a password is strong, weak, or reused
# OOP Concept: Abstraction (complex checks hidden in methods)
# ============================================================

import re

class PasswordAuditor:

    # Minimum requirements for a strong password
    MIN_LENGTH    = 8
    COMMON_PASSWORDS = [
        "password", "123456", "abc123", "qwerty",
        "password1", "111111", "iloveyou", "admin",
        "welcome", "monkey", "dragon", "letmein"
    ]

    # ── Check strength of a single password ─────────────────
    def check_strength(self, password):
        issues = []

        if len(password) < self.MIN_LENGTH:
            issues.append(f"Too short (min {self.MIN_LENGTH} characters)")

        if not re.search(r"[A-Z]", password):
            issues.append("No uppercase letter")

        if not re.search(r"[a-z]", password):
            issues.append("No lowercase letter")

        if not re.search(r"[0-9]", password):
            issues.append("No number")

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            issues.append("No special character (!@#$ etc)")

        if password.lower() in self.COMMON_PASSWORDS:
            issues.append("This is a very common password")

        if issues:
            return "WEAK", issues
        else:
            return "STRONG", []

    # ── Check for reused passwords across credentials ────────
    def check_reuse(self, credentials, encryptor):
        seen      = {}
        reused    = []

        for cred in credentials:
            plain = encryptor.decrypt(cred.get_encrypted_password())
            if plain in seen:
                reused.append((cred.get_site(), seen[plain]))
            else:
                seen[plain] = cred.get_site()

        return reused

    # ── Audit all saved credentials ──────────────────────────
    def audit_all(self, credentials, encryptor):
        print("\n  ════════════════════════════════")
        print("         PASSWORD AUDIT REPORT    ")
        print("  ════════════════════════════════")

        for cred in credentials:
            plain         = encryptor.decrypt(cred.get_encrypted_password())
            status, issues = self.check_strength(plain)
            icon           = "✅" if status == "STRONG" else "⚠️ "

            print(f"\n  {icon} {cred.get_site()}  ({status})")
            for issue in issues:
                print(f"     → {issue}")

        # Check reused
        reused = self.check_reuse(credentials, encryptor)
        if reused:
            print("\n  ⚠️  REUSED PASSWORDS DETECTED:")
            for site1, site2 in reused:
                print(f"     → {site1}  and  {site2}  use same password!")

        print("\n  ════════════════════════════════\n")
