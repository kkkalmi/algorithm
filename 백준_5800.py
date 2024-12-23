all = int(input())

for i in range(all):
    arr = list(map(int, input().split()))
    stu_num = arr[0]
    arr.remove(arr[0])
    stu_max = max(arr)
    stu_min = min(arr)
    result = sorted(arr, reverse=True)

    gap = []
    for j in range(len(result)):
        if j == len(result)-1:
            break
        else:
            gap.append(result[j] - result[j+1])
    
    print("Class {}".format(i+1))
    print("Max {}, Min {}, Largest gap {}".format(stu_max, stu_min, max(gap)))