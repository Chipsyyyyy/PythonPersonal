from collections import Counter

def most_freq_num(nums):
    counter = Counter(nums)

    most_freq = counter.most_common(1)[0][0]
    # .most_common(1) and .most_common(1)[0] return value and freq
    # .most_common(1)[0][0] returns value only
    
    print(most_freq)

most_freq_num([1, 1, 5, 7, 10])
