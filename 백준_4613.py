import sys

data = sys.stdin.read().strip()

lines = data.split("\n")

dic = {chr(i): i - 64 for i in range(65, 91)}

for line in lines:
    sum = 0
    if line.strip() == "#":
        break
    else:
        arr = list(line)
        for i in range(len(arr)):
            if arr[i] == ' ':
                continue
            else:
                sum += dic[arr[i]] * (i + 1)
        print(sum)