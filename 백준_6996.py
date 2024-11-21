all = int(input())

for i in range(all):
    N, M = input().split()
    
    a = sorted(N)
    b = sorted(M)
    
    if a == b:
        print("{} & {} are anagrams.".format(N,M))
    else:
        print("{} & {} are NOT anagrams.".format(N,M))