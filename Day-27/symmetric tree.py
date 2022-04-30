class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left,right):
            if left==None and right==None:
                return True
            if left!=None and right!=None:
                if left.val==right.val:
                    return dfs(left.left,right.right) and dfs(right.left,left.right)
            return False
        if root==None:
            return True
        left=root.left
        right=root.right
        return dfs(left,right)