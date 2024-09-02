# 두 정수 입력받기
A, B = map(int, input().split())

# 비교하기
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')