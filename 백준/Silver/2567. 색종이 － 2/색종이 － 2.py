def count(arr):
    cnt = 0
    for lst in arr:
        for i in range(1, len(lst)):
            if lst[i-1] != lst[i]:  # 현재 인덱스 값이 이전의 값과 다르면 경계선 (둘레)
                cnt += 1
    return cnt

N = int(input())
arr = [[0]*102 for _ in range(102)]
# 해당 범위 1로 채우기
for _ in range(N):
    sj, si = map(int, input().split())
    for i in range(si, si+10):
        for j in range(sj, sj+10):
            arr[i][j] = 1

arr_t = list(zip(*arr)) # 전치행렬
result = count(arr) + count(arr_t)
print(result)