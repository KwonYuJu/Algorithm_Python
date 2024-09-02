while True: # 무한 루프
  # 입력 받은 세 변의 길이 정렬하여 할당
  a, b, c = sorted(map(int, input().split())) 
  
  if a == 0 and b == 0 and c == 0: # '0 0 0'이 입력되는 경우 종료
    break
  
  # 피타고라스 정리
  if a**2 + b**2 == c**2:
    print("right")
  else:
    print("wrong")