import math

A, B, V = map(int, input().split())

N = math.ceil((V-A)/(A-B)) + 1
print(N)