import math


def execute_optimal(arr, s):
    min_length = math.inf
    window_start = 0

    for window_end in range(len(arr)):
        s -= arr[window_end]

        while s <= 0:
            min_length = min(min_length, window_end - window_start + 1)

            s += arr[window_start]
            window_start += 1

    return min_length if min_length != math.inf else 0


if __name__ == '__main__':
    print(execute_optimal([2, 1, 5, 2, 3, 2], 7))
    print(execute_optimal([2, 1, 5, 2, 8], 7))
    print(execute_optimal([3, 4, 1, 1, 6], 8))
    print(execute_optimal([3, 4, 1, 1, 6], 100))
