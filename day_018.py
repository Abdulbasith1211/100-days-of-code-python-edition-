#DAY 19   {PROBLEM SOLVING - STACKS}



#PROBLEM : https://www.hackerrank.com/challenges/equal-stacks/problem
import math
import os
import random
import re
import sys


def equalStacks(h1, h2, h3):
    if __name__ == "__main__":
        stack = []
    ops_cnt = int(input().strip())
    max_elem = 0
    
    for _ in range(ops_cnt):
        args = list(map(int, input().strip().split()))
        
        if args[0] == 1:
            max_elem = max(max_elem, args[1])
            stack.append(args[1])
        if args[0] == 2:
            if stack.pop() == max_elem:
                if len(stack) > 0:
                    max_elem = max(stack)
                else:
                    max_elem = 0
        if args[0] == 3:
            print(max_elem)



#PROBLEM :   https://www.hackerrank.com/challenges/balanced-brackets/problem


import sys

def isBalanced(s):
    stack = []
 
    for letter in s:
        if letter == '{':
            stack.append(1)
        elif letter == '[':
            stack.append(2)
        elif letter == '(':
            stack.append(3)
        elif letter == '}':
            if len(stack) == 0:
                return False
            if stack.pop() != 1:
                return False
        elif letter == ']':
            if len(stack) == 0:
                return False
            if stack.pop() != 2:
                return False
        elif letter == ')':
            if len(stack) == 0:
                return False
            if stack.pop() != 3:
                return False
 
    return len(stack) == 0

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        result = isBalanced(s)
        if result is True:
            print('YES')
        else:
            print('NO')