# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = collections.deque([root])

        while queue:
            if queue[-1]:
                res.append(queue[-1].val)
            for i in range(len(queue)):
                curr = queue.popleft() 
                if curr:
                    queue.append(curr.left) if curr.left else None
                    queue.append(curr.right) if curr.right else None
        return res