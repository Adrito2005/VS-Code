a = int(input("Enter the length of the list "))

l = []
s = []
for i in range(a):
    for k in range(a):
        x = int(input("Enter the elements of ", i, "X", k, " th list"))
        s.append(x)
    l.append(s)
    s = []

sum, sum2 = 0, 0

for x in range(a):
    sum += l[x][x]
    sum2 += l[x][a-1-x]

print("sum of both diagonals ", (sum+sum2))
