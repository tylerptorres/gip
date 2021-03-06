from TreeNode import TreeNode


def find_path(root, sequence):
    if root is None or root.val != sequence[0]:
        return False

    if (
        root.left is None
        and root.right is None
        and len(sequence) == 1
        and root.val == sequence[0]
    ):
        return True

    return find_path(root.left, sequence[1:]) or find_path(root.right, sequence[1:])


# O(N) T & S
def find_path_optimal(root, sequence, idx=0):
    if root is None or root.val != sequence[idx] or idx >= len(sequence):
        return False

    if root.left is None and root.right is None:
        return idx == len(sequence) - 1

    return find_path(root.left, sequence, idx + 1) or find_path(
        root.right, sequence, idx + 1
    )


if __name__ == "__main__":

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print(find_path(root, [1, 0, 1]))
