class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        head=root
        if root==None:
            return
        if root.left==None and root.right==None:
            return root
        #if root.left!=None and root.right!=None:
            
        #root=root.left
    
        root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return head
    
            