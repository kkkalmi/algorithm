a = [int(input()) for _ in range(9)]
b = sum(a) - 100

for i in a:
    for j in a:
        if i + j == b and i != j:
            a.remove(i)
            a.remove(j)
            break

print(*a, sep='\n')