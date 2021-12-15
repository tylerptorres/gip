
# O(N + M) T | O(N + M) S
def execute(firstList, secondList):
    merged = []
    idx1, idx2 = 0, 0
    start, end = 0, 1

    def interval_overlap(interval_one, interval_two):
        a_overlaps_b = interval_one[start] >= interval_two[start] and \
            interval_one[start] <= interval_two[end]

        # check if intervals overlap and firstList[j]'s start time lies within the other interval_two[i]
        b_overlaps_a = interval_two[start] >= interval_one[start] and \
            interval_two[start] <= interval_one[end]

        return a_overlaps_b or b_overlaps_a

    def merge_intersection(interval_one, interval_two):
        return [max(interval_one[start], interval_two[start]), min(interval_one[end], interval_two[end])]

    while idx1 < len(firstList) and idx2 < len(secondList):
        interval_one, interval_two = firstList[idx1], secondList[idx2]
        if interval_overlap(interval_one, interval_two):
            merged.append(merge_intersection(interval_one, interval_two))

        if interval_one[end] < interval_two[end]:
            idx1 += 1
        else:
            idx2 += 1
    return merged


if __name__ == '__main__':

    print(execute([[1, 3], [5, 6]], [[2, 3], [5, 7]]))
    print(execute([[1, 3], [5, 7], [9, 12]], [[5, 10]]))
    print(execute([[1, 5], [5, 7], [9, 12]], [[5, 10]]))
