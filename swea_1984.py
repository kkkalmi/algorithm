T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    
    arr.remove(max(arr))
    arr.remove(min(arr))
    
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        
    arrange = round(sum / len(arr))
    
    print(f"#{test_case} {arrange}")