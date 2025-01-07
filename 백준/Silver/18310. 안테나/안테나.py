import sys
input = sys.stdin.readline

N = int(input())

houses = list(map(int,input().split()))
houses.sort()
point = (len(houses) + 1) // 2

print(houses[point-1])