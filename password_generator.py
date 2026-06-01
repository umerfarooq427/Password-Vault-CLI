# ============================================================
# password_generator.py
# Generates a strong random password
# OOP Concept: Abstraction (user just calls generate())
# ============================================================

import secrets
import string

class PasswordGenerator:

    def __init__(self, length=12):
        self.__length = length

    # ── Generate a strong random password ───────────────────
    def generate(self):
        characters = (
            string.ascii_uppercase +   # A-Z
            string.ascii_lowercase +   # a-z
            string.digits          +   # 0-9
            "!@#$%^&*()"               # special chars
        )

        # Make sure at least one of each type is included
        password = [
            secrets.choice(string.ascii_uppercase),
            secrets.choice(string.ascii_lowercase),
            secrets.choice(string.digits),
            secrets.choice("!@#$%^&*()")
        ]

        # Fill the rest randomly
        for _ in range(self.__length - 4):
            password.append(secrets.choice(characters))

        # Shuffle so the required chars aren't always at start
        secrets.SystemRandom().shuffle(password)

        return "".join(password)

    # ── Change the length ────────────────────────────────────
    def set_length(self, length):
        self.__length = length
