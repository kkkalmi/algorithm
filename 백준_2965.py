arr = list(map(int, input().split()))

a = arr[1] - arr[0]
b = arr[2] - arr[1]

result = 0
if a > b:
    result = arr[1] - arr[0] - 1
else:
    result = arr[2] - arr[1] - 1

print(result)