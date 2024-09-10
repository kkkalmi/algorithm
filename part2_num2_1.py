def solution(L, x):
    num = 0
    for i in range(len(L)):
        if L[i] > x:
            num = i
            break
        elif L[i] < x:
            num += 1
            
    if(num == len(L)):
        num = len(L)
    
    L.insert(num , x)
    
    answer = L
    return answer