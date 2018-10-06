class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def haspathsum(node, sum):
    if node == None:
        return True
    else:
        sum -= node.data
        
        # check if the current node is leaf
        if node.left == None and node.right == None and sum ==0:
            return True
        elif node.left:
            sum = sum or haspathsum(node.left, sum)
        elif node.right:
            sum = sum or haspathsum(node.right, sum)
        return sum

s = 21
root = Node(10) 
root.left = Node(8) 
root.right = Node(2) 
root.left.right = Node(5) 
root.left.left = Node(3) 
root.right.left = Node(2) 
  
if haspathsum(root, s): 
    print "There is a root-to-leaf path with sum %d" %(s) 
else: 
    print "There is no root-to-leaf path with sum %d" %(s) 
  