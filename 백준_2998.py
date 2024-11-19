num = list(map(int, input()))

while True:
    if len(num) % 3 != 0:
        num.insert(0, 0)
    else:
        break

sum = 0
my_result = []
while True:
    result = "".join(map(str, num[sum:sum+3]))
    if result == '000':
        my_result.append(0)
    elif result == '001':
        my_result.append(1)
    elif result == '010':
        my_result.append(2)
    elif result == '011':
        my_result.append(3)
    elif result == '100':
        my_result.append(4)
    elif result == '101':
        my_result.append(5)
    elif result == '110':
        my_result.append(6)
    else:
        my_result.append(7)
    sum+=3
    if sum == len(num):
        break

print("".join(map(str, my_result)))