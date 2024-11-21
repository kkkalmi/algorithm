i = 1

while True:
    a = input()
    b = input()
    if a == "END" and b == "END":
       break
    else:
        A = sorted(list(a))
        B = sorted(list(b))
        if A == B:
            print("Case {}: same".format(str(i)))
        elif A != B:
            print("Case {}: different".format(str(i)))
        i += 1