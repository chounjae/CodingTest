import sys
from collections import Counter
input = sys.stdin.readline

arr= list((map(int, input().strip())))

print(*sorted(arr, reverse=True), sep="")