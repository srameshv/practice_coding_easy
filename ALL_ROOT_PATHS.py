class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        return ["{}->{}".format(root.val, val) for val in self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)]        

# Always for Pre-order traversal
# Find the path with sum.
def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        elif not root.left and not root.right:
            if root.val == sum:
                return True
            else:
                return False
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

# check if any paths in a tree has the given sum 

# Python program to find if there is a root to sum path 
  
# A binary tree node  
class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
  
"""  
 Given a tree and a sum, return true if there is a path from the root 
 down to a leaf, such that adding up all the values along the path 
 equals the given sum. 
   
 Strategy: subtract the node value from the sum when recurring down, 
 and check to see if the sum is 0 when you run out of tree. 
"""
# s is the sum 
def hasPathSum(node, s): 
      
    # Return true if we run out of tree and s = 0  
    if node is None: 
        return (s == 0) 
  
    else: 
        ans = 0 
          
        # Otherwise check both subtrees 
        subSum = s - node.data  
          
        # If we reach a leaf node and sum becomes 0, then  
        # return True  
        if(subSum == 0 and node.left == None and node.right == None): 
            return True 
  
        if node.left is not None: 
            ans = ans or hasPathSum(node.left, subSum) 
        if node.right is not None: 
            ans = ans or hasPathSum(node.right, subSum)


# All paths from root in binary tree 
def printRoute(stack, root): 
    if root == None: 
        return
          
    # append this node to the path array 
    stack.append(root.data) 
    if(root.left == None and root.right == None): 
          
        # print out all of its  
        # root - to - leaf 
        print(' '.join([str(i) for i in stack])) 
          
    # otherwise try both subtrees 
    printRoute(stack, root.left) 
    printRoute(stack, root.right) 
    stack.pop()