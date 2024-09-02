n = int(input())
for _ in range(n):
    lst = list(input())
    score = 0       # 연속된 o를 계산할 변수
    sum_score = 0   # 최종 점수를 저장할 변수
    for i in lst:
        if i == 'O':
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)
