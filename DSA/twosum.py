def two_sums(nums, target):
    # {value : index}
    seen = {}

    for i, num in enumerate(nums): # enumerate allows looping through any iterable while being able to track the index and value
        complement = target - num

        # If complement is already in the dictionary we found the pair
        if complement in seen:
            return [seen[complement], i]
        # Otherwise, add the current number and it's index into the dictionary
        seen[num] = i

    return []

def test_two_sum():
    # Test Case 1: Standard case
    nums1 = [2, 7, 11, 15]
    target1 = 9
    assert two_sums(nums1, target1) == [0, 1], f"Test 1 Failed: {two_sums(nums1, target1)}"

    # Test Case 2: Numbers are not adjacent
    nums2 = [3, 2, 4]
    target2 = 6
    assert two_sums(nums2, target2) == [1, 2], f"Test 2 Failed: {two_sums(nums2, target2)}"

    # Test Case 3: Same number needed twice (but different indices)
    nums3 = [3, 3]
    target3 = 6
    assert two_sums(nums3, target3) == [0, 1], f"Test 3 Failed: {two_sums(nums3, target3)}"

    # Test Case 4: No solution exists
    nums4 = [1, 2, 3]
    target4 = 7
    assert two_sums(nums4, target4) == [], f"Test 4 Failed: {two_sums(nums4, target4)}"

    print("All test cases passed!")

test_two_sum()