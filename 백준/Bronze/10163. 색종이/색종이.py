N = int(input())
arr = [[0]*1001 for _ in range(1001)]

# arr에 색종이 번호 채우기
for n in range(1, N+1):
    sj, si, w, h = map(int, input().split())
    for i in range(si, si+h):
        arr[i][sj:sj+w] = [n]*w

# cnts 빈도수 배열 사용해서 색종이 번호 count (arr한 번만 순회)
cnts = [0]*(N+1)
for lst in arr:
    for i in lst:     
        cnts[i] += 1  
print(*cnts[1:], sep='\n')