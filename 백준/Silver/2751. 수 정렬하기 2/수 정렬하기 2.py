import sys
input = sys.stdin.readline

N = int(input())
lst = [0]*N

for i in range(N):
    lst[i] = int(input())

lst.sort()
print(*lst, sep="\n")