import re

# 🚨 Common prompt injection patterns
BLOCKED_PATTERNS = [
    r"ignore previous instructions",
    r"disregard above",
    r"system:",
    r"assistant:",
    r"reveal .* prompt",
    r"bypass security",
]

def contains_prompt_injection(text: str) -> bool:
    text_lower = text.lower()
    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, text_lower):
            return True
    return False


def strip_html(text: str) -> str:
    return re.sub(r"<.*?>", "", text)


def sanitize_input(text: str) -> dict:
    if not text or len(text.strip()) == 0:
        return {"error": "Input cannot be empty"}

    # Remove HTML
    clean_text = strip_html(text)

    # Detect prompt injection
    if contains_prompt_injection(clean_text):
        return {"error": "Potential prompt injection detected"}

    return {"clean": clean_text.strip()}