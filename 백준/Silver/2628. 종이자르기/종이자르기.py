C, R = map(int, input().split())
N = int(input())

# 가로, 세로 따로 리스트 만들어서 자르는 위치 append하고 sort하기
c_lst = [0,C]
r_lst = [0,R]
for _ in range(N):
    t, n = map(int, input().split())
    if t == 0:
        r_lst.append(n)
    if t == 1:
        c_lst.append(n)
c_lst.sort()
r_lst.sort()

# 리스트에서 길이 구해서 최대 길이 찾기
# 세로 최대 길이
c_mx = 0
for i in range(1, len(c_lst)):
    c_mx = max(c_mx, c_lst[i]-c_lst[i-1])
# 가로 최대 길이
r_mx = 0
for i in range(1, len(r_lst)):
    r_mx = max(r_mx, r_lst[i]-r_lst[i-1])

print(c_mx * r_mx)