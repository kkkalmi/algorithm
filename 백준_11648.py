num = input()

sad = 0

while True:
    a = 1
    if len(num) == 1:
        break
    else:
        for i in num:
            a = a * int(i)
        num = str(a)
        sad += 1

print(sad)