import re

BLOCK_PATTERNS = [
    r"ignore (all )?previous instructions",
    r"reveal (system )?prompt",
    r"developer mode",
    r"print hidden",
    r"show.*api key",
    r"override restrictions",
    r"debug mode"
]

def is_malicious(prompt: str) -> bool:
    prompt = prompt.lower()
    for pattern in BLOCK_PATTERNS:
        if re.search(pattern, prompt):
            return True
    return False

def sanitize_input(prompt: str) -> str:
    # Basic sanitization (can be extended)
    return prompt.strip()

if __name__ == "__main__":
    user_input = input("Enter prompt: ")

    if is_malicious(user_input):
        print("Blocked: Potential prompt injection detected.")
    else:
        clean = sanitize_input(user_input)
        print("Safe input:", clean)
