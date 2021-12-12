

def execute(arr):
    result = []
    positive_index = 0

    for i in range(len(arr)):
        positive_index = i
        if arr[positive_index] >= 0:
            break

    left = positive_index - 1
    right = positive_index

    while left >= 0 and right < len(arr):
        if arr[right]**2 <= arr[left]**2:
            result.append(arr[right]**2)
            right += 1
        else:
            result.append(arr[left]**2)
            left -= 1

    # while right < len(arr):
    #     result.append(arr[right]**2)
    #     right += 1

    # while left >= 0:
    #     result.append(arr[left]**2)
    #     left -= 1

    if left < 0:
        result += [num**2 for num in arr[right:]]
    if right >= len(arr):
        result += [arr[i]**2 for i in range(left, -1, -1)]
    return result


# O(N) T | O(N) S
def execute_two(arr):
    result = [0] * len(arr)
    highest_square_idx = len(arr) - 1
    left, right = 0, len(arr) - 1

    while left <= right:
        left_square, right_square = arr[left]**2, arr[right]**2

        if left_square > right_square:
            result[highest_square_idx] = left_square
            left += 1
        else:
            result[highest_square_idx] = right_square
            right -= 1

        highest_square_idx -= 1

    return result


if __name__ == '__main__':
    print(execute_two([-2, -1, 0, 2, 3]))
    print(execute_two([-3, -1, 0, 1, 2]))
    print(execute_two([-3, -1, 0, 4, 8]))
