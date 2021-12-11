
# O(N) T | O(1)
def execute_optimal(arr, k):
    running_sum = max_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        running_sum += arr[window_end]

        if window_end >= k - 1:
            max_sum = max(max_sum, running_sum)
            running_sum -= arr[window_start]
            window_start += 1

    return max_sum


if __name__ == '__main__':
    print(execute_optimal([2, 1, 5, 1, 3, 2], 3))
    print(execute_optimal([2, 3, 4, 1, 5], 2))
