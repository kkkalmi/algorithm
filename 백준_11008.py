all = int(input())

for i in range(all):
    N, M = input().split()
    sum = N.count(M)
    result = [word for word in N.split(M) if word]
    for k in range(len(result)):
        for j in range(len(result[k])):
            sum += 1
    print(sum)