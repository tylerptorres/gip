from math import dist, inf


# O(N) T | O(1) S
def execute_optimal(s, k):
    max_length = -inf
    window_start = 0
    distinct_map = {}

    for window_end in range(len(s)):
        if s[window_end] not in distinct_map:
            distinct_map[s[window_end]] = 0
        distinct_map[s[window_end]] += 1

        while len(distinct_map) > k:
            distinct_map[s[window_start]] -= 1
            if distinct_map[s[window_start]] == 0:
                distinct_map.pop(s[window_start])
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length


if __name__ == '__main__':
    print(execute_optimal("araaci", 2))
    print(execute_optimal("araaci", 1))
    print(execute_optimal("cbbebi", 3))
    print(execute_optimal("cbbebi", 10))
