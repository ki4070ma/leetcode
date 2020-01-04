# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        self.target_list = []

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        # print(type(root))
        # print(root)
        self.showNodeVal(root)
        return sum([x for x in self.target_list if x >= L and x <= R])

    def showNodeVal(self, node: TreeNode):
        if node.left:
            self.showNodeVal(node.left)
        self.target_list.append(node.val)
        if node.right:
            self.showNodeVal(node.right)

# From discuss
class Solution:

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        target_list = []
        return sum(self.store_target_list(root, L, R, target_list))

    def store_target_list(self, node, L, R, target_list):
        if node.left:
            self.store_target_list(node.left, L, R, target_list)
        if node.val >= L and node.val <= R:
            target_list.append(node.val)
        if node.right:
            self.store_target_list(node.right, L, R, target_list)
        return target_list
