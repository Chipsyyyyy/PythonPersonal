from collections import Counter

def same_letters(s):
    counts = {}

    for c in s:
        counts[c] = counts.get(c, 0) + 1 # .get() searches for a value and takes 2 arguments
        # num is the value i am searching for
        # 0 is the default if the value isn't found
        # if the number is already in the dictionary it returns the current count
    
    for c in s:
        if counts[c] == 1:
            return c
        
    return None


def same_letters_lib(s):
    counts = Counter(s)

    return next((char for char in s if counts[char] == 1), None)

def test():
    same_letters()