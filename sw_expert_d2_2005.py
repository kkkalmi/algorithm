#2005. 파스칼의 삼각형 D2

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    
    array1 = [[0] * n for _ in range(n)]
    
    for i in range(n):
        array1[i][0] = 1
        
    for i in range(1,n):
        for j in range(0, n-1):
            array1[i][j+1] = array1[i-1][j] + array1[i-1][j+1]
            
    print(f"#{test_case}")
    for i in range(n):
          for j in range(n):
              if(array1[i][j] > 0):
                  print(array1[i][j], end=' ')
          print()