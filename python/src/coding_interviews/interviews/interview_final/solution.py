def wordPattern(pattern: str, s: str) -> bool:
    """
    Determines if the string `s` follows the pattern `pattern`.

    Here follow means a full match, such that there is a bijection
    between a letter in pattern and a non-empty word in `s`.

    Example:
    Input: `pattern = "abba"`, `s = "dog cat cat dog"`
    Output: `true`
    """
    words = s.split(" ")

    # If we can't map each word to a letter in the pattern.
    if len(words) != len(pattern):
        return False

    # If the number of unique words is different than the number
    # of unique letters.
    if len(set(words)) != len(set(pattern)):
        return False

    words_to_letter: dict[str, str] = dict()
    for word, letter in zip(words, pattern):
        if word not in words_to_letter:
            words_to_letter[word] = letter
        elif words_to_letter[word] != letter:
            return False

    return True
