from TreeNode import TreeNode


def execute(root):
    if root is None:
        return

    all_paths = []
    helper(root, all_paths)

    return all_paths


def helper(root, all_paths, current=[]):
    current.append(root.val)

    if root.left is None and root.right is None:
        all_paths.append(list(current))
    else:
        helper(root.left, all_paths, current)
        helper(root.right, all_paths, current)

    current.pop()


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(execute(root))
