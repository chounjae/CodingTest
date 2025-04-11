import sys
from collections import deque
input = sys.stdin.readline

repeat = int(input())

stack = deque([])
for i in range(repeat):

    keyword = input()

    if "push" in keyword :
        keyword, value = keyword.split()
        stack.append(int(value))
    elif "pop" in keyword :
        if len(stack) > 0:
            print(stack.popleft())
        else :
            print(-1)
    elif "size" in keyword :
        print(len(stack))
    elif "top" in keyword :
        if len(stack) > 0:
            print(stack[-1])
        else :
            print(-1)
    elif "empty" in keyword :
        if len(stack) > 0:
            print(0)
        else :
            print(1)
    elif "front" in keyword :
        if len(stack) > 0:
            print(stack[0])
        else :
            print(-1)
    elif "back" in keyword :
        if len(stack) > 0:
            print(stack[-1])
        else :
            print(-1)