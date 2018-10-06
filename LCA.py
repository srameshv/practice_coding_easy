class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Method 1 - O(h) T&S time complexity , check if the node is none, if node<n1 and n2-go right , go left , else return node
def lca(root, n1, n2):
    if root == None:
        return None
    
    if root.data < n1 and root.data < n2:
        lca(root.right, n1, n2)
    
    if root.data > n1 and root.data > n2:
        lca(root.left, n1, n2)
    
    else:
        return root

    #ITERATE TO SAVE SPACE METHOD 2 save space 
    while(root != NULL):
        if root.data < n1 and root.data < n2:
            root = root.right
        if root.data > n1 and root.data > n2:
            root = root.left
        else:
            break
    return root

# Method 2 -using parent pointer. find the depth diff and move the deep pointer, make it the same depth 
def find_depth(node): # since the parent pointer is present, utilize that property
    depth = 0
    while(node != NULL):
        depth+=1
        node = node.parent
    return depth

def lca_parent(root, n1, n2):
    
    # find the depths of n1 and n2 and difference
    depth_difference = abs(depth(n1) - depth(n2))

    if depth_difference < 0 : # means n2 is deeper, so swap n1 and n2 , so we only need to move one
        Node temp = n1
        n1 = n2
        n2 = temp
        depth_difference = -depth_difference

     while(depth_difference >=0):
         n1 = n1.parent
         depth_difference-=1

    # Now n1 and n2 are at the same level, implement the lca logic here
    while(n1 != NULL or n2 != NULL):
        if (n1 == n2):
            return n1
        n1 = n1.parent
        n2 = n2.parent

    return NULL

    
    

