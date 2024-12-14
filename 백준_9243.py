N = int(input())

a, b = list(input()), list(input())

for _ in range(N):
    for i in range(len(a)):
        if a[i] == '1':
            a[i] = '0'
        else:
            a[i] = '1'
            
print("Deletion succeeded" if a==b else "Deletion failed")