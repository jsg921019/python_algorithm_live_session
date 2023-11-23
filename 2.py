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