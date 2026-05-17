def twosum(input, target):
    left = 0
    right = len(input) - 1

    while left < right: #
        current_sum = input[left] + input[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1