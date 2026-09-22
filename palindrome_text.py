"""Case-insensitive palindrome checks for words and phrases."""


def is_palindrome(text):
    """Ignore non-alphanumeric characters; an empty phrase is a palindrome."""
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    normalized = "".join(char for char in text.casefold() if char.isalnum())
    reversed_text = normalized[::-1]
    return normalized == reversed_text
