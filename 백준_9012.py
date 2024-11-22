num = int(input())

for i in range(num):
    n = input()
    no = 0
    arr = []
    for j in n:
        if j == '(':
            arr.append(i)
        else:
            if len(arr) == 0:
                no += 1
            else:
                arr.pop()
    if len(arr) >= 1 or no >= 1:
        print("NO")
    else:
        print("YES")
            