
# O(N^2) T | O(1) S
def execute_optimal(sorted_arr):
    idx = 0

    while idx < len(sorted_arr) - 1:
        while idx < len(sorted_arr) - 1 and sorted_arr[idx] == sorted_arr[idx+1]:
            sorted_arr.pop(idx+1)

        idx += 1
    return len(sorted_arr)


def execute_optimal_two(sorted_arr):
    idx = 0

    while idx < len(sorted_arr) - 1:
        if sorted_arr[idx] == sorted_arr[idx+1]:
            sorted_arr.pop(idx+1)
        else:
            idx += 1
    return len(sorted_arr)


# O(N) T | O(1)
def execute(sorted_arr):
    next_non_duplicate = 1

    for i in range(len(sorted_arr) - 1):
        # we have unique elements next to each other, so swap values and move up the place where we will possibly start replacing duplicates
        if sorted_arr[i] != sorted_arr[i + 1]:
            sorted_arr[next_non_duplicate] = sorted_arr[i + 1]
            next_non_duplicate += 1  # increment to say that everything before this pointer is unique

    return next_non_duplicate


if __name__ == '__main__':
    print(execute_optimal([2, 3, 3, 3, 6, 9, 9]))
    print(execute_optimal([2, 2, 2, 11]))
    print(execute_optimal_two([2, 3, 3, 3, 6, 9, 9]))
    print(execute([2, 2, 2, 11]))
    print(execute([2, 2, 2, 11, 13, 13, 13, 13, 14, 15, 16]))
