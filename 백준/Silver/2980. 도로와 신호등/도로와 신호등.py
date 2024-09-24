N, L = map(int, input().split())
# 출발지(0미터 지점, 빨간불 대기시간 0, 초록불 바로 지나감 1) + 각 신호등 위치,정보 + 도착지(L미터 지점)
arr = [[0,0,1]]+[list(map(int, input().split())) for _ in range(N)]+[[L,0,1]]

cnt = 0     # 경과 시간
for i in range(1, len(arr)): # 첫 번째 신호등부터 도착점 전까지의 신호등 순회
    d, r, g = arr[i]         # [[0, 0, 1], [3, 5, 5], [5, 2, 2], [10, 0, 1]]
    cnt += (d - arr[i-1][0]) # 위치 간 이동거리 계산
    cnt += max(0, r - (cnt % (r+g)))    # 대기시간 계산
    # cnt % (r + g)이 r보다 작으면 빨간불 -> r - (cnt % (r + g))만큼 대기
    # cnt % (r + g)이 r보다 크거나 같으면 초록불 -> 대기시간 0 근데 음수가 나올 수도 있어서 max
print(cnt)