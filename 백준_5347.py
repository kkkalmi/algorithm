num = int(input())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

for i in range(num):
    N, M = map(int, input().split())
    lcm = N * M // gcd(N,M)
    print(lcm)