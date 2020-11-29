from queue import Queue

class Node:
    def __init__(self, value:int, left, right):
        self.left = left
        self.right = right
        self.value = value

"""
        1
   2        3
40   5        6
7           8
Print in zigzag order 1 3 2 40 5 6 8 7
"""

tree = Node(1, 
            Node(2, 
                Node(40, 
                    Node(7, None, None), 
                    None
                    ), 
                Node(5, None, None)
                ), 
            Node(3,
                None,
                Node(6, 
                    Node(8, None, None), 
                    None
                    )
                )
            )

main_queue = Queue()
main_queue.put([tree])
queue2 = Queue()
count = 0

while(not main_queue.empty()):

    items = main_queue.get()
    queue2.put(items)

    if (len(items) == 0):
        break

    q = []
    for node in items:
        if(node.left):  
            q.append(node.left)
        if (node.right):
            q.append(node.right)

    main_queue.put(q)


count = 1
while(not queue2.empty()):
    items = queue2.get()
    if count:
        start, end, step = 0, len(items), 1
    else:
        start, end, step = len(items) - 1, -1, -1
    
    for i in range(start,end,step):
        print(items[i].value)
    
    count ^= 1