from collections import Counter

N_dict = Counter(input())
M_dict = Counter(input())

print(sum((N_dict-M_dict).values()) + sum((M_dict-N_dict).values()))