#재귀적 이진 탐색 구현하기
def solution(L,x, l, u):
    if(l == u and L[l] != x):
        return -1
    mid = (l + u) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return solution(L, x, l, mid - 1)
    else:
        return solution(L, x, mid + 1, u)