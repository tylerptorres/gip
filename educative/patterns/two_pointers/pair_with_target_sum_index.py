
# O(N) T | O(1) S
def execute_optimal(sorted_arr, target):
    left, right = 0, len(sorted_arr)-1

    while left < right:
        current_sum = sorted_arr[left] + sorted_arr[right]
        if current_sum == target:  # return indices of where the pair values are
            return [left, right]

        if current_sum < target:
            left += 1
        else:
            right -= 1

    return -1


# O(N) T | O(N) S
def execute(sorted_arr, target):
    target_map = {}

    for idx, val in enumerate(sorted_arr):
        if target - val in target_map:
            return [target_map[target-val], idx]

        target_map[val] = idx

    return -1


if __name__ == '__main__':
    print(execute_optimal([1, 2, 3, 4, 6], 6))
    print(execute_optimal([2, 5, 9, 11], 11))
    print(execute([1, 2, 3, 4, 6], 6))
    print(execute([2, 5, 9, 11], 11))
