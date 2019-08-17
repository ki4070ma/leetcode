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
