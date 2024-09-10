N = int(input())
arr = [[0]*102 for _ in range(102)]

# 넓이에 해당하는 좌표 1로 채우기
for _ in range(N):
    sj, si = map(int, input().split())
    for i in range(si, si+10):
        for j in range(sj, sj+10):
            arr[i][j] = 1

    # 1 다 합하기 (넓이)
    ans = 0
    for lst in arr:
        ans += sum(lst)

print(ans)