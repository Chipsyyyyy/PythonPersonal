from collections import Counter

# def firstUniqueChar(string):
#     counts = {}
    
#     for letter in string:
#         counts[letter]+=1
    
#     for i in range(string):
#         if(counts[string[i]] == 1):
#             return i
    
#     return len(string)

def firstUniqueChar(input_string):
    counts = Counter(input_string)

    for index, char in enumerate(input_string):
        if counts[char] == 1:
            return index

    return len(input_string)

print(firstUniqueChar("acabcd"))