
# O(N^2) T | S
def find_sum(lst, k):

    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == k:
                return [lst[i], lst[j]]

    return -1


# O(N log N) + O(N) T | O(1) S
def find_sum_sorted(lst, k):
    lst.sort()  # O(N log N) + O(N)

    left_idx = 0
    right_idx = len(lst) - 1

    while left_idx < right_idx:
        if lst[left_idx] + lst[right_idx] == k:
            return [lst[left_idx], lst[right_idx]]

        if lst[left_idx] + lst[right_idx] < k:
            left_idx += 1
        else:
            right_idx += 1

    return -1


print(find_sum([1, 21, 3, 14, 5, 60, 7, 6], 81))
print(find_sum_sorted([1, 21, 3, 14, 5, 60, 7, 6], 81))
