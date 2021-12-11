# O(N * k) T | O(k) S
def execute_brute(arr, k):
    res = []

    # elementary way
    """
    for i in range(len(arr) - k + 1):
        total = 0
        for j in range(i, i + k):
            total += arr[j]
        res.append(total / k)
    """

    # pythonic way
    for i in range(len(arr) - k + 1):
        res.append(sum(arr[i:i+k]) / k)

    return res


# O(N) T | O(k) S
def execute_optimal_one(arr, k):
    average_array = []
    total = sum(arr[:k])
    average_array.append(total / k)

    for idx in range(1, len(arr) - k + 1):
        total = total - arr[idx - 1] + arr[idx + k - 1]
        average_array.append(total / k)

    return average_array


# O(N) T | O(k) S
def execute_optimal_two(arr, k):
    average_array = []
    window_start = total = 0

    for window_end in range(len(arr)):
        total += arr[window_end]

        if window_end >= k - 1:
            average_array.append(total / k)
            total -= arr[window_start]
            window_start += 1

    return average_array


if __name__ == '__main__':
    print(execute_brute([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))
    print(execute_optimal_two([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))

# length of array = 9, max index = 8
# Need the last element in the window at the start of the looping to be at 4
# 0 - 4 = 5 element window
