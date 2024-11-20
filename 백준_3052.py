import sys
a = [int(x) for x in sys.stdin.read().split()]
result_list = []
for i in range(len(a)):
    result = a[i] % 42
    result_list.append(result)

my_list = set(result_list)

print(len(my_list))