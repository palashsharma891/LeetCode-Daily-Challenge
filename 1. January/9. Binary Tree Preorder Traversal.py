# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, valval=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, rootshroot: Optional[TreeNode]) -> List[int]:

        def dfs(root, ans):
            if not root:
                return
            ans += [root.val]
            dfs(root.left, ans)
            dfs(root.right, ans)

        ans = []

        dfs(rootshroot, ans)

        return ans
