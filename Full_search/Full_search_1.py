#최소직사각형 찾기
def solution(sizes):
    length = len(sizes)
    mx = []
    mn = []
    for i in range(length):
        if(sizes[i][0] >= sizes[i][1]):
            mx.append(sizes[i][0])
            mn.append(sizes[i][1])
        else:
            mx.append(sizes[i][1])
            mn.append(sizes[i][0])
    
    mx.sort()
    mn.sort()

    
    return max(mx) * max(mn)