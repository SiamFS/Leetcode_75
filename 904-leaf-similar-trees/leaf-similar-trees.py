
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):

        lst1=[]
        lst2=[]
        def leaf_node(root,lst):
            if root is None:
                return 
            elif root.left==None and root.right==None:
                    lst.append(root.val)
                    return
            leaf_node(root.left,lst)
            leaf_node(root.right,lst)
        
        leaf_node(root1,lst1)
        leaf_node(root2,lst2)
    
        return lst1==lst2
        
