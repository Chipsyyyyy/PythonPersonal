#Merge Sort - Divide and Conquer: Splitting the Array in half until it is left with single elements and merge it all back together
import random

def mergeSort(nums): # [4, 1, 3, 2]
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    l = mergeSort(nums[:mid])
    r = mergeSort(nums[mid:])

    return merge(l, r)
    
def merge(left, right):
    sorted_array = []
    
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])
        return sorted_array
    
def main():
    nums = []
    for _ in range(1, 10):
        num = random.randint(1, 100)
        nums.append(num)
    print(nums)
    print(mergeSort(nums))

if __name__ == "__main__":
    main()

