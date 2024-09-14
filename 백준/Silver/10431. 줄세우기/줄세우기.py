P = int(input())
for tc in range(1, P+1):
    lst = list(map(int, input().split()))[1:]

    cnt = 0     # 학생들이 뒤로 물러선 횟수(내 앞에 나보다 큰 숫자 개수) 초기화
    for i in range(1, 20):      # i : 현재 위치의 학생
        for j in range(0, i):   # j : i 앞에 있는 학생들
            if lst[i] < lst[j]: # i번째 학생이 j번째 학생보다 작으면, i번째 학생이 앞에 서야 하므로 한칸씩 뒤로 물러남
                cnt += 1        # 물러선 횟수를 1 증가
    print(f'{tc} {cnt}')