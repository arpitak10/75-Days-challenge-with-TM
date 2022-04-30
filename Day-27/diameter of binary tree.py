class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            nonlocal max_dia
            if root==None:
                return 0
            left=height(root.left)
            right=height(root.right)
            curr_dia=left+right
            max_dia=max(curr_dia,max_dia)
            return max(left,right)+1
        max_dia=0
        height(root)
        return max_dia