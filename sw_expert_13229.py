T = int(input())

for test_case in range(1, T + 1):
    dates = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    n = input()
 
     
    if( n == "SUN"):
        print(f"#{test_case} {7}")
    else:
        print(f"#{test_case} {7 - (dates.index(n)+1)}")