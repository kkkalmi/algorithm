def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

num1, num2 = map(int, input().split())
print(gcd(num1,num2))
print(num1*num2//gcd(num1,num2))