from collections import Counter

def single_number(nums, target):
    counts = {}

    # Count the occurences of each number
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    
    for num, count in counts.items():
        if count == 1:
            return num

    return None

def single_number_lib(nums):
    counts = Counter(nums)

    for num, count in counts.items():
        if count == 1:
            return num
