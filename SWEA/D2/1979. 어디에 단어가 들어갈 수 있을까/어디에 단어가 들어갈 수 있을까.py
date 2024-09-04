def count(arr):
    ans = 0
    for lst in arr:
        cnt = 0
        for j in range(len(lst)):
            if lst[j] != 0:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0
    return ans

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+1)] # 우측/아래 0 채우기
    arr_t = list(zip(*arr))     # 전치행렬
    result = count(arr) + count(arr_t)

    print(f'#{tc} {result}')