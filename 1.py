# solution 1
def solution(expression):
    
    if expression[-1] != '0':
        return "ERROR"
    
    ans = 0
    sign = 1
    prev = None
    
    sign_dict = {'+': 1, '-': -1}
    
    for c in expression:
        if c == '0':
            if prev == '0':
                ans += sign
        else:
            if prev in ('-', '+'):
                return "ERROR"
            sign = sign_dict[c]

        prev = c
        
    return str(ans)

# solution 2
def solution(expression):
    
    l = []
    prev = None
    sign = 1
    
    for c in expression:
        
        if c == '0':
            if prev == '0':
                l[-1] += sign
            else:
                l.append(0)
        else: 
            if prev == '+' or prev == '-':
                return 'ERROR'
            else:
                if c == '+':
                    sign = 1
                else:
                    sign = -1
        
        prev = c
        
    if prev =='+' or prev == '-':
        return 'ERROR'

    return str(sum(l))