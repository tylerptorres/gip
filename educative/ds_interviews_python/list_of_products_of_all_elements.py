import math
# O(N^2) T | O(N) S


def find_product_brute(lst):
    result = [0 for i in range(len(lst))]

    for i in range(len(lst)):
        running_product = 1
        for j in range(len(lst)):
            if i == j:
                continue

            running_product *= lst[j]
        result[i] = running_product

    return result


# O(N) T | O(1) S ( not counting the output arrays when there are zeros )
def find_product_improved(nums):
    zeroExists = isAllZeros = False
    total_product = 1
    zero_index = -1

    for idx, number in enumerate(nums):
        if number == 0 and zeroExists:
            isAllZeros = True
            break
        elif number == 0:
            zeroExists = True
            zero_index = idx
        else:
            total_product *= number

    if isAllZeros:
        return [0] * len(nums)

    if zeroExists:
        return [total_product if i == zero_index else 0 for i in range(len(nums))]

    for idx, num in enumerate(nums):
        nums[idx] = int(total_product / num)

    return nums


# O(N) T | O(1) Space ( not counting result array )
def find_product_optimal(nums):
    res = []

    left = 1
    for i in range(len(nums)):
        res.append(left)
        left = left * nums[i]

    right = 1
    for i in reversed(range(len(nums))):
        res[i] = res[i] * right
        right = right * nums[i]

    return res


print(find_product_brute([1, 2, 3, 4]))
print(find_product_brute([1, 2, 3, 5, 8]))
print()
print(find_product_optimal([1, 2, 3, 4]))
print(find_product_optimal([1, 2, 3, 5, 8]))
print(find_product_optimal([4, 2, 1, 5, 0]))
print(find_product_optimal([4, 2, 0, 5, 0]))
print(find_product_optimal([-1, 1, 0, -3, 3]))
