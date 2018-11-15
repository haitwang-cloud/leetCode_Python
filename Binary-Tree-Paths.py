# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 执行时间为60ms的案例
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        self.trace(root,'',res)
        
    def trace(self,root,path,res):
        if root:
            if root.left or root.right:
                self.trace(root.left,path+str(root.val)+'->',res)
                self.trace(root.right,path+str(root.val)+'->',res)
            else:
                res.append(path+str(root.val))

