


def execute(arr, target):
    triplets = 0
    arr.sort() # O(N log N)

    for i in range(len(arr) - 2):
        triplets += get_triplets(arr, i, target)

    return triplets

def get_triplets(arr, idx, target):
    left, right = idx + 1, len(arr) - 1
    triplet_count = 0

    while left < right:
        triplet_sum = arr[idx] + arr[left] + arr[right]

        if triplet_sum < target:
            triplet_count += right - left
            left += 1
        else: # triplet_sum >= target
            right -= 1
        


    return triplet_count

if __name__ == '__main__':
    print(execute([-1, 0, 2, 3], 3))
    print(execute([-1, 4, 2, 1, 3], 5))