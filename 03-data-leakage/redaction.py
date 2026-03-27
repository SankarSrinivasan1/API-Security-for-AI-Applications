import re

SENSITIVE_PATTERNS = [
    r"sk-[a-zA-Z0-9]{20,}",
    r"api[_-]?key\s*=\s*[a-zA-Z0-9]+",
    r"password\s*=\s*\S+"
]

def redact(text: str) -> str:
    for pattern in SENSITIVE_PATTERNS:
        text = re.sub(pattern, "[REDACTED]", text, flags=re.IGNORECASE)
    return text

if __name__ == "__main__":
    sample = "API key is sk-1234567890abcdef"
    print(redact(sample))
