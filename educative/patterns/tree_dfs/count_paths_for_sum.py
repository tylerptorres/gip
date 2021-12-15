from TreeNode import TreeNode


""" 
Algorithm only works when all nodes in the tree have positive values.
O(4^k) T | O(N) S
O(4^k) == O(N^2) where N = 2^k
 """


def execute(root, path_sum):
    if root is None:
        return 0

    return dfs(root, path_sum)


def dfs(root, path_sum):

    if root is None:
        return 0

    if path_sum - root.val == 0:
        return 1

    including_left_parent = dfs(root.left, path_sum - root.val)
    excluding_left_parent = dfs(root.left, path_sum)

    including_right_parent = dfs(root.right, path_sum - root.val)
    excluding_right_parent = dfs(root.right, path_sum)

    return including_left_parent + including_right_parent + excluding_left_parent + excluding_right_parent


if __name__ == '__main__':

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(execute(root, 11)))

    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(3)
    print("Tree has paths: " + str(execute(root, 12)))
