class Stack(object):
    def __init__(self):
        self.items = []
    def push(self, data):
        self.items.append(data)
    def pop(self):
        print("Popped ", self.items[::0])
        return self.items[len(items)-1]

# celebrity problem
# IF A knows B, then A is not B might be
# IF A doesn't know B, then A might be and B definitley is not
# make sure we have the celebrity

def isCelebrity(N): # party of N people
    s = Stack()
    # push everyone to the stack
    for i in range(N):
        s.push(i)
    
    # until the stack is left with only one person
    while s.size > 1:
        person1 = s.pop()
        person2 = s.pop()
        if knows(person1, person2): # person1 knows person2
            s.push(person2)
        else:
            s.push(person1)
    # Step 5 : Check if the last 
    # person is celebrity or not
    for (int i = 0; i < n; i++) 
    {
        // If any person doesn't
        //  know 'c' or 'a' doesn't 
        // know any person, return -1
        if (i != c && (knows(c, i) || 
                        !knows(i, c)))
            return -1;
    }
    return c;

        
    
    
    