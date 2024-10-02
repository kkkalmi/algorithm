T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    number = list(map(int, input().split()))
    max = 0
    min = 0
    for i in range(0, n):
        if( number[i] > max ):
            max = number[i]
            min = number[i]


    for i in range(0, n):
        if( number[i] < min ):
            min = number[i]
     
    print("#{0} {1}".format(test_case, max - min))