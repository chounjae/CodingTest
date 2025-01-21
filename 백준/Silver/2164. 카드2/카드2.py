import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
deck = deque([i for i in range(1,n+1)])

while 1 :
    if len(deck) > 2 :
        deck.popleft()
        switch = deck.popleft()
        deck.append(switch)
    elif len(deck) == 2 :
        print(deck[1])
        break
    else :
        print(deck[0])
        break