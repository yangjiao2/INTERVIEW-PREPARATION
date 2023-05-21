#!/bin/python3

import math


def fakenews(text: str) -> str:
    # Write your code here
    stack = []
    op = None
    reverse = 1
    val = None
    
    def update(op, v):
        if len(stack) == 0:
            stack.append(v)
        
        if op == '&':
            prev = stack.pop()
            if prev == -1 or v == -1:
                stack.append(-1)
            elif prev == 1 and v == 1:
                stack.append(1)
            else:
                stack.append(0)
        elif op == '|':
            prev = stack.pop()
            if prev == 1 or v == 1:
                stack.append(1)
            elif prev == 0 or v == 0:
                stack.append(0)
            else:
                stack.append(-1)
        print (stack)
            
    i = 0
    while i <= len(text):
        c = text[i]
 
        if c == '(':
            val, index = fakenews(text[i+1:])
   
            i += (index + 1)
            print (val, index, i) # 1 6 9
            reverse = 1
        elif c == ')':
            update(op, val * reverse)
            res = stack[0] if (len(stack) > 0) else val
            print ('res', res, i + 1) # 1 6
            return res, i + 1
        elif c == '!':
            reverse = -1
        elif c == '?':
            val = 0
        elif c == '&' or c == '|':
            update(op, val * reverse)
            reverse = 1
            op = c
        elif c == 'T':
            val = 1
        elif c == 'F':
            val = -1
            
        i += 1

    update(op, val)
    
    res = stack[0] if (len(stack) > 0) else val
    print (res)
    if res == 1:
        return 'T'
    elif res == -1:
        return 'F'
    else: 
        return '?'
    
print ('->', fakenews('T&(!T|!F)'))

