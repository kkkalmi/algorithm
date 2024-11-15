T = int(input())

for test_case in range(1, T + 1):
    h, m, h1, m2 = map(int, input().split())
    
    result_hour = h + h1
    
    result_minute = m + m2
    
    if result_hour > 12:
        result_hour = result_hour % 12
    if result_minute > 60:
        result_hour += 1
        result_minute = result_minute % 60
        
    print(f"#{test_case} {result_hour} {result_minute}")