class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

min = -44444
max = 44444
def isbst(node):
    return isbstutil(node, min, max)

# METHOD 1 => Time Complexity - O(n)
def isbstutil(node, min, max):
    if node == Null:
        return True
    
    if node.data < min or node.data > max:
        return False

    return (isbstutil(node.left, min, node.data-1) and isbstutil(node.right, node.data+1, max))
  

# METHOD 2 => Time Complexity - O(n) InOrder Traversal
# Just like Inorder traversal left->root->right
prev = None
def isbst(root):
    # prev is a global variable initialize it to none
    global prev
    prev = None
    return isbst_rec(root)

def isbst_rec(root):
    global prev

    #Always first step is to check if root is none
    if root == None:
        return False
    
    # Check the left one as its Inorder traversal
    if isbst_rec(root.left) is False:
        return False
    
    # check the current node
    if prev.data and prev.data > root.data:
        return False

    # check the right subtree
    prev = root
    return isbst_rec(root.right)