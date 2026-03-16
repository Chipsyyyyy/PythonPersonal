from collections import Counter

def same_letters(s):
    counts = {}

    for c in s:
        counts[c] = counts.get(c, 0) + 1
    
    for c in s:
        if counts[c] == 1:
            return c
        
    return None


def same_letters_lib(s):
    counts = Counter(s)

    return next((char for char in s if counts[char] == 1), None)

def test():
    same_letters()