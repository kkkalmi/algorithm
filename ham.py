import sys.stdin 

T = int(input())

for tc in range(1, T + 1):
    N, L = map(int, input().split())
    ingredients = [list(map(int, input().split())) for _ in range(N)] # T:맛 점수, K:재료 칼로리

max_taste_score = 0

for bitmask in range(1 << N):
    total_taste = 0
    total_calories = 0

for i in range(N):
    if bitmask & (1 << i):
        total_taste += ingredients[i][0]
        total_calories += ingredients[i][1]

    if total_calories > L:
        continue

    if total_calories <= L:
        max_taste_score = max(max_taste_score, total_taste)

print("#{} {}".format(tc, max_taste_score))