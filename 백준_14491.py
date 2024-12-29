def factorial(n):
    if n <= 0:
        return ""
    else:
        return factorial(n // 9) + str(n%9)
    
user = int(input())
print(factorial(user))