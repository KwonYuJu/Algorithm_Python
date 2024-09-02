N = int(input())
words = set()           # set(): 중복 허용 X

for _ in range(N):      # 입력 받은 모든 단어를 set에 추가하여 중복 제거
    input_word = input().strip()
    words.add(input_word)

words = list(words)     # 집합을 리스트로 변환

words.sort()            # 사전 순으로 먼저 정렬

words = sorted(words, key=len)  # 길이 기준으로 재정렬

for input_word in words:        # 정렬된 단어들 출력
    print(input_word)