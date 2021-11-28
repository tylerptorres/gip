
# O(N + M) T | S
def merge(lst1, lst2):

    if not lst1 or not lst2:
        return lst1 if len(lst2) == 0 else lst2

    ptr1, ptr2 = 0, 0
    result = []

    while ptr1 < len(lst1) and ptr2 < len(lst2):

        if lst1[ptr1] <= lst2[ptr2]:
            result.append(lst1[ptr1])
            ptr1 += 1
        else:
            result.append(lst2[ptr2])
            ptr2 += 1

    if ptr1 != len(lst1):
        result += lst1[ptr1:]

    if ptr2 != len(lst2):
        result += lst2[ptr2:]

    return result


# O(N * M) T | O(M) S
# Further reduced to
    # O(N^2) T | O(M) S
def merge_inplace(lst1, lst2):

    idx1, idx2 = 0, 0

    while idx1 < len(lst1) and idx2 < len(lst2):

        if lst1[idx1] <= lst2[idx2]:
            idx1 += 1
        else:
            lst1.insert(idx1, lst2[idx2])
            idx1 += 1
            idx2 += 1

    if idx2 < len(lst2):
        lst1 += lst2[idx2:]

    return lst1


"""
- Tradeoffs
    - Merging in place reduces space but increases time complexity

"""

print(merge([1, 3, 4, 5], [2, 6, 7, 8]))
print(merge([1, 3, 4], [2, 6, 8, 9, 10]))
print(merge([1, 3, 3, 4], [2, 2, 7, 11]))
print()
print(merge_inplace([1, 3, 4, 5], [2, 6, 7, 8]))
print(merge_inplace([1, 3, 4], [2, 6, 8, 9, 10]))
print(merge_inplace([1, 3, 3, 4], [2, 2, 7, 11]))
