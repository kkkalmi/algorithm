all = int(input())

for i in range(all):
    N, M = map(int, input().split())
    arr = []
    for i in range(N):
        arr.append(int(input()))
    arr2 = set(arr)
    print(N - len(arr2))