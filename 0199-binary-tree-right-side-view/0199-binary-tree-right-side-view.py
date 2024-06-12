# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        
        li=[]
        li2=[]
        def right_view(root,c,li,li2):
            if root==None:
               return 
            if c not in li:
               li2.append(root.val)
               li.append(c)
            right_view(root.right,c+1,li,li2)
            right_view(root.left,c+1,li,li2) 
        right_view(root,0,li,li2)
        return li2

        