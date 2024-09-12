#이진탐색

def solution(L, x):
    lower = 0
    upper = len(L) - 1
    while lower <= upper:
        midle = (lower + upper) // 2
        if(L[midle] == x):
            return midle
        elif(L[midle] < x):
            lower = midle + 1
        else:
            upper = midle - 1
    return -1