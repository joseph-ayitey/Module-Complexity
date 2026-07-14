def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.

    Before: O(n²) — for each character, `letter.lower() not in s` scans the entire
    string (O(n)) to check membership. Over n characters that is O(n²) total.

    After: O(n) — precompute a set of all characters in s once (O(n), O(n) space).
    Each membership check is then O(1), making the overall loop O(n).
    """
    char_set = set(s)
    only_upper = set()
    for letter in s:
       if is_upper_case(letter) and letter.lower() not in char_set:
           only_upper.add(letter)
    return len(only_upper)


def is_upper_case(letter: str) -> bool:
    return letter == letter.upper()
