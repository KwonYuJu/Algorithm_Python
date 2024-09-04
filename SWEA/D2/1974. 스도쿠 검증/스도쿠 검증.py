def rows(arr):
    # 가로줄 검사
    for row in arr:
        if len(set(row)) != 9:
            return False
    return True

def columns(arr):
    # 세로줄 검사 (zip 전치)
    arr_t = list(zip(*arr))
    for col in arr_t:
        if len(set(col)) != 9:
            return False
    return True

def boxes(arr):
    # 3x3 박스 검사
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            box = []
            for x in range(3):
                for y in range(3):
                    box.append(arr[i + x][j + y])
            if len(set(box)) != 9:
                return False
    return True

def sudoku(arr):
    # 모든 검사를 통과해야 유효한 스도쿠
    if rows(arr) and columns(arr) and boxes(arr):
        return 1
    else:
        return 0

# 테스트 케이스 입력 처리
T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = sudoku(arr)
    print(f"#{tc} {result}")