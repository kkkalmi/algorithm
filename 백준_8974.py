N, M = map(int, input().split())

user_list = []

for i in range(1, M+1):
    if len(user_list) < M:
        for _ in range(i):
            user_list.append(i)

print(sum(user_list[N-1:M]))