# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def rightSideView(self, root):
        self.lst = []
        
        def traverse(node, level):
            if node is None:
                return []
    
            if level == len(self.lst):
                self.lst.append(node.val)

            traverse(node.right, level + 1)
            traverse(node.left, level + 1)
        
        traverse(root, 0)
        return self.lst