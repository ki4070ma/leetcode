# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# From solution

class Solution:
    def constructMaximumBinaryTree(self, nums):
        if nums is None:
            return None

        new_val = max(nums)
        split_index = nums.index(new_val)
        node = TreeNode(new_val)
        if len(nums[:split_index]):
            node.left = self.constructMaximumBinaryTree(nums[:split_index])
        if len(nums[split_index + 1:]):
            node.right = self.constructMaximumBinaryTree(nums[split_index + 1:])

        return node

# Failed by own solution
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        max_val = max(nums)
        max_idx = nums.index(max_val)
        root_node = TreeNode(max_val)
        print(nums[:max_idx])
        print(nums[max_idx + 1:])
        root_node.left = self.store_val_to_list(sorted(nums[:max_idx], reverse=True), left=True)
        root_node.right = self.store_val_to_list(sorted(nums[max_idx + 1:], reverse=True), left=True)
        print(root_node.right)
        return root_node

    def store_val_to_list(self, nums, left):
        if len(nums) == 0:
            return None
        ret = TreeNode(nums[0])
        if len(nums[1:]) > 0:
            if left:
                ret.right = self.store_val_to_list(nums[1:], left=True)
            else:
                ret.left = self.store_val_to_list(nums[1:], left=True)
        return ret