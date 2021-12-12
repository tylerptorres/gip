
# O(N) T | O(1) S
def execute_optimal(sorted_arr, target):
    left, right = 0, len(sorted_arr) - 1

    while left < right:
        current_sum = sorted_arr[left] + sorted_arr[right]
        if current_sum == target:
            return [sorted_arr[left], sorted_arr[right]]

        if current_sum < target:
            left += 1
        else:
            right -= 1

    return -1


if __name__ == '__main__':
    print(execute_optimal([1, 2, 3, 4, 6], 6))
