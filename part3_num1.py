# 피보나치 수열

def solution(x):
    if(x == 0):
        return 0
    elif(x <= 2 and x > 0):
        return 1
    else:
        return solution(x - 2) + solution(x - 1)