T = int(input())

for test_case in range(1, T + 1):
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    grade_list = []
    N, K = map(int, input().split())
    for _ in range(N):
        medium, last, work = map(int, input().split())
        sum = (medium * 0.35) + (last * 0.45) + (work * 0.2)
        grade_list.append(sum)
 
    target = grade_list[K-1]
    grade_list.sort(reverse=True)
    rate = N // 10
    idx = grade_list.index(target) // rate
    print(f"#{test_case} {grades[idx]}")