import re


def _validate_email(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?<!\.[.])[^\s@]*$"
    if re.match(pattern=pattern, string=email):
        return True
    return False
