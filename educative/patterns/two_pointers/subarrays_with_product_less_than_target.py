def execute(arr, target):
    products = []
    left = 0
    current_product = 1

    for right, value in enumerate(arr):
        # calculate current sum
        current_product *= value

        # one size length array
        if value < target:
            products.append([value])

        #  criteria to move left pointer if product is >= target, move left pointer and divide by that number,
        while left < right and current_product >= target:
            # divide by left pointer and move it up
            current_product //= arr[left]
            left += 1
        # add subarray to product
        if right - left + 1 > 1:
            products.append(arr[left : right + 1])

    return products

    # How do we address duplicates?
    # Something to clarify with the interviewer


if __name__ == "__main__":
    print(execute([2, 5, 3, 10], 30))
    print(execute([8, 2, 6, 5], 50))
    print(execute([1, 2, 3], 0))
