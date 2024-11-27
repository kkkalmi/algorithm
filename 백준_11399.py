n = int(input())
data = list(map(int, input().split()))
data.sort()
sum = 0
sum2 = 0

list = []
for i in range(n):
    sum += data[i]
    list.append(sum)

for i in range(n):
    sum2 += list[i]
print(sum2)