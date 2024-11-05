T = int(input())

for t in range(1, T + 1):
    N = int(input()) 
    A = list(map(int, input().split()))  
    B = list(map(int, input().split()))  

    switch_count = 0  

    for i in range(N):
        if A[i] != B[i]:  
            switch_count += 1  
            for j in range(i, N):
                A[j] = 1 - A[j]  

    print(f"#{t} {switch_count}")