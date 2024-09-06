T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N: 행의 수, M: 열의 수
    arr = [input() for _ in range(N)]  # N개의 문자열로 된 깃발 배열 입력

    min_paint = float('inf')  # 최소로 다시 칠해야 하는 칸 수를 저장할 변수

    # i는 흰색으로 칠할 마지막 줄의 인덱스
    for i in range(N-2):
        # j는 파란색으로 칠할 마지막 줄의 인덱스
        for j in range(i+1, N-1):
            paint_count = 0  # 다시 칠해야 하는 칸 수를 저장할 변수

            # 흰색으로 칠할 줄들: 0번째 줄부터 i번째 줄까지
            for s in range(i+1):
                for k in range(M):
                    if arr[s][k] != 'W':  # 흰색이 아닌 칸은 다시 칠해야 함
                        paint_count += 1

            # 파란색으로 칠할 줄들: i+1번째 줄부터 j번째 줄까지
            for s in range(i+1, j+1):
                for k in range(M):
                    if arr[s][k] != 'B':  # 파란색이 아닌 칸은 다시 칠해야 함
                        paint_count += 1

            # 빨간색으로 칠할 줄들: j+1번째 줄부터 마지막 줄까지
            for s in range(j+1, N):
                for k in range(M):
                    if arr[s][k] != 'R':  # 빨간색이 아닌 칸은 다시 칠해야 함
                        paint_count += 1

            # 가장 적게 칠하는 경우를 찾음
            min_paint = min(min_paint, paint_count)

    print(f'#{tc} {min_paint}')
