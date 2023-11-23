# solution 1
def solution(receipt, inventory):
    inven = set(inventory)
    do_again = True
    while do_again:
        do_again = False
        for i1, i2, r in receipt:
            if i1 in inven and i2 in inven:
                inven.remove(i1)
                inven.remove(i2)
                inven.add(r)
                do_again = True
    return sorted(inven)


# solution 2
def solution(receipt, inventory):
    
    inven = set(inventory)
    d = {}
    
    for i1, i2, r in receipt:
        
        d[i1] = [i1, i2, r]
        d[i2] = [i1, i2, r]
        
        if i1 in inven and i2 in inven:
            inven.remove(i1)
            inven.remove(i2)
            inven.add(r)
            if r in d:
                _i1, _i2, _r = d[r]
                receipt.append(d[r])
                del d[_i1]
                del d[_i2]
                
    return sorted(inven)

# solution 3

from collections import defaultdict, deque

def solution(receipt, inventory):
    
    receipt = [tuple(com) for com in receipt]

    item2node = {}
    for i1, i2, r in receipt:
        item2node[i1] = (i1, i2, r)
        item2node[i2] = (i1, i2, r)
        
    graph = defaultdict(list)
    num_childs = defaultdict(int)
    for i1, i2, r in receipt:
        if r in item2node:
            graph[(i1, i2, r)].append(item2node[r])
            num_childs[item2node[r]] += 1

    order = []
    queue = deque()
    
    for com in receipt:
        if num_childs[com] == 0:
            queue.append(com)
    
    while queue:
        com = queue.popleft()
        order.append(com)
        for parent in graph[com]:
            num_childs[parent] -= 1
            if num_childs[parent] == 0:
                order.append(parent)
                
    inven = set(inventory)
    for i1, i2, r in order:
        if i1 in inven and i2 in inven:
            inven.remove(i1)
            inven.remove(i2)
            inven.add(r)
            
    return sorted(inven)