n = int(input())
for i in range(0,n):
    c = int(input())
    list = [0,0,0,0,0,0,0,0]
    while ( c != 0 ):
        if( c >= 50000 ):
           list[0] = c // 50000
           c = c % 50000
        elif( c >= 10000):
           list[1] = c // 10000
           c = c % 10000
        elif( c >= 5000):
           list[2] = c // 5000
           c = c % 5000
        elif( c >= 1000):
           list[3] = c // 1000
           c = c % 1000
        elif( c >= 500 ):
           list[4] = c // 500
           c = c % 500
        elif( c >= 100 ):
           list[5] = c // 100
           c = c % 100
        elif(c >= 50):
           list[6] = c // 50
           c = c % 50
        elif( c >= 10):
           list[7] = c // 10
           c = c % 10
    print("#",i+1)
    print(list)
        