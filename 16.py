a = int(input("Enter the length of the list "))

l = []
s = []
for i in range(a):
    for k in range(a):
        x = int(input("Enter the elements of ", i, "X", k, " th list"))
        s.append(x)
    l.append(s)
    s = []

flag = 0
sum = 0

for i in l:
    if flag == 0 or flag == len(l)-1:
        for k in i:
            sum += k
    else:
        sum = sum + i[0] + i[len(i)-1]
    flag += 1


print(sum)
