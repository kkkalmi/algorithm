#버블 숫자 정렬
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    number = list(map(int, input().split()))
     
    for i in range(len(number)):
        for j in range(len(number)-1):
            if(number[j] > number[j+1]):
                temp = number[j]
                number[j] = number[j+1]
                number[j+1] = temp
    print("#{0} {1}".format(test_case, ' '.join(map(str, number))))
    # ///////////////////////////////////////////////////////////////////////////////////