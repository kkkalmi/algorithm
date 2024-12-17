n, m = map(int, input().split())

a = ''
b = ''
new_result = ''

for i in range(n):
    user = input()
    a += user

for i in range(n):
    result = input()
    b += result

for i in range(n*m):
    new_result = new_result + a[i] + a[i]

if b == new_result:
    print("Eyfa")
else:
    print("Not Eyfa")