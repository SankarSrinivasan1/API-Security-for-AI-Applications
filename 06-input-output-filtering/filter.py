import re

BLOCK_INPUT = [
    r"ignore instructions",
    r"reveal prompt"
]

BLOCK_OUTPUT = [
    r"sk-[a-zA-Z0-9]+",
    r"api key"
]

def filter_input(text: str) -> bool:
    for pattern in BLOCK_INPUT:
        if re.search(pattern, text.lower()):
            return False
    return True

def filter_output(text: str) -> str:
    for pattern in BLOCK_OUTPUT:
        text = re.sub(pattern, "[BLOCKED]", text, flags=re.IGNORECASE)
    return text

if __name__ == "__main__":
    user_input = input("Input: ")

    if not filter_input(user_input):
        print("Blocked input")
    else:
        output = "API key is sk-123456"
        print(filter_output(output))
