#SW_EXPERT_ACADEMY D2 1204 최빈수 구하기
T = int(input())

for test_case in range(1, T + 1):
    test_num = int(input())
     
    grades = list(map(int, input().split()))
     
    score = [0]*101
     
    max_num = 0
     
    for grade in grades:
        score[grade] += 1
        if score[grade] >= score[max_num]:
            max_num = grade
             
    print(f"#{test_num} {max_num}")