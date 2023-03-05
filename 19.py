a = int(input("Enter a number "))
s = 0
i = a
k = 0
if (a < 9 or a == 0):
    print("It is a neven number")
    exit()
else:
    while i != 0:
        s += k
        k = i % 10
        i = i//10

if a % s == 0 or a == 0:
    print("Yes it is neven number")
else:
    print("It is not neven number")
