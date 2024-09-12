N = int(input())
arr = [[0]*1001 for _ in range(1001)]

# arr에 색종이 번호 채우기
for n in range(1, N+1):
    sj, si, w, h = map(int, input().split())
    for i in range(si, si+h):
        for j in range(sj, sj+w):
            arr[i][j] = n

# 색종이 번호 count (면적 구하기)
for n in range(1, N+1):
    cnt = 0
    for lst in arr:
        cnt += lst.count(n)
    print(cnt)