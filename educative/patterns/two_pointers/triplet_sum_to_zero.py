
# O(N^2) | O(N) S
def execute(arr):
    result = []
    arr.sort()  # O(N * log(N)) T | O(N) S

    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left, right = i + 1, len(arr) - 1
        while left < right:
            triplet_sum = arr[i] + arr[left] + arr[right]

            if triplet_sum == 0:
                # retain that triplet and apply logic to forego duplicates
                result.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1

                while arr[left] == arr[left - 1] and left < right:
                    left += 1
                while arr[right] == arr[right + 1] and left < right:
                    right -= 1

            elif triplet_sum < 0:
                left += 1
            else:
                right -= 1

    return result


if __name__ == '__main__':
    print(execute([-3, 0, 1, 2, -1, 1, -2]))
    print(execute([-5, 2, -1, -2, 3]))
    print(execute([-5, 2, -1, -2, 2, 3, 3]))
    print(execute([-1, 0, 1, 2, -1, -4]))

    # -5, -2, -1, 2, 3

    # eval => -5, -2, 3 = -4
    # eval => -5, -1, 3 =
    # eval => -5, -1, 3

    # trioplet_sum < 0 --> increment left pointer
    #              > 0 --> incremenet right pointer

    # triplet_sum == 0 -->
    # if there are duplicates, special logic to move past that so no triplet is processed more than once
