# Two nodes of a BST are swapped, correct the BST
# Solution is to set 3 pointers => first, middle and last.
# During inorder traversal , when we find a node , where the current value 
# is less than the previous value , the set the first as the prev node and 
# middle as current, first = prev, middle = current . When we find the second point 
# where the current < prev , then set last as the current.
# Now, once we've all the values set, if the swapped nodes are adjacent, then we
# won't find the last pointer.So in that case , swap first and middle Else swap 
# first and last.

# TIME COMPLEXITY = O(n)

# Do bst traversal and set the pointers.
def check_bstUtil(root):
    if root != NULL:
        check_bstUtil(root.left) # first step in inorder traversal

        if prev != NULL and prev > root.data : # violation of the BST rule
            # Check if its the first violation
            if first == NULL:
                first = prev
                middle = root
            else: # second violation
                last = root
        
        # now this node becomes prev for the right hand traversal
        prev =  root
        check_bstUtil(root.right) # right hand traversal of the tree

def correct_bst(root):
    
    # the call for check_bstUtil goes from here
    # so set the pointers to NULL
    first = middle = last = NULL
    correct_bstUtil(root)

    # Correct the tree
    if(first != NULL and last != NULL):
        temp = Node()
        temp = first
        first = last
        last = temp
    elif(first != NULL and middle != NULL):
        temp = Node()
        temp = first
        first = middle
        middle = temp
