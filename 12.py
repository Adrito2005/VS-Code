a = int(input("Which number you want to check "))
s = 0
flag = 0
while a > 9:
    for i in list(str(a)):
        s += int(i)**2
    if (s == 1):
        flag = 1
        break
    a = s
    s = 0
if (flag == 1):
    print("Happy Number Indeed")
else:
    print("So sad numbers")
