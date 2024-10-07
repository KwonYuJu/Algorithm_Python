import math

N = int(input())
A_lst = list(map(int, input().split()))
B, C = map(int, input().split())

ans = N
for a in A_lst:
    if a-B > 0:
        ans += math.ceil((a-B)/C)     
print(ans)