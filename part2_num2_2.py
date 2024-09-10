def solution(L, x):
    list = []
    
    if x in L:
        for i in range(len(L)):
            if(L[i] == x):
                list.append(i)
            
    if x not in L:
        list.append(-1)
    
            
    answer = list
    return answer