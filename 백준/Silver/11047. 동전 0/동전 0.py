N, K = map(int, input().split())
coin = 0
value = [int(input()) for _ in range(N)]
value.sort(reverse=True)

while K:
    for i in value:
        coin += K // i
        K %= i

print(coin)