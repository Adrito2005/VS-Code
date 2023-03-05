def binary(l, x):
    u = 0
    e = len(l)-1
    s = (u+e)//2
    while x != l[s]:
        if (x > l[s]):
            u = s
        else:
            e = s
        s = (u+e)//2
    print(s)


a = [2, 12, 3, 4, 654, 9, 87, 987, 2, 3, 654, 8, 7]
a.sort()
print(a)

x = int(input("Enter what you want to know"))
binary(a, x)
