
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


print(merge([1, 3, 4, 5], [2, 6, 7, 8]))
print(merge([1, 3, 4], [2, 6, 8, 9, 10]))
print(merge([1, 3, 3, 4], [2, 2, 7, 11]))
