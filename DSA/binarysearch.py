import random

def search(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            print(f"Target at index: {mid}")
            return mid
        
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    print("Target is not present")   
    return -1

def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    l = mergeSort(nums[:mid])
    r= mergeSort(nums[mid:])
    
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
    for _ in range(100):
        num = random.randint(1, 100)
        nums.append(num)
    target = random.randint(1, 100)
    print(mergeSort(nums))
    print(target)
    search(mergeSort(nums), target)

if __name__ == "__main__":
    main()