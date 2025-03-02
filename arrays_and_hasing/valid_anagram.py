def is_anagram_sorted(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

print(is_anagram_sorted("anagram", "nagaram"))  # True

