class Solution:
    def isidentical(self,root,subRoot):
        if root==None and subRoot==None:
            return True
        if root and subRoot==None:
            return False
        if root==None and subRoot!=None:
            return False
        if root.val==subRoot.val:
            return self.isidentical(root.left,subRoot.left) and self.isidentical(root.right,subRoot.right)
        #print(root,subRoot)
        #return False   
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root==None and subRoot:
            return False
        if root and subRoot==None:
            return False
        if root==None and subRoot==None:
            return True
        #return root
        #print(root)
    
        return self.isidentical(root,subRoot) or (root.left and self.isSubtree(root.left,subRoot)) or (root.right and self.isSubtree(root.right,subRoot))