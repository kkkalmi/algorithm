T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
     
    arr = sorted(list(map(int, input().split())))
     
    for i in range(N):
        prod = (arr[i] // M) * K
        if prod < i+1:
            print(f"#{test_case} Impossible")
            break
    else:
        print(f"#{test_case} Possible")