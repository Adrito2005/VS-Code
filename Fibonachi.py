l = [1, 1]
n = int(input("Length of the fibonachi series "))
s = 0
for i in range(n):
    s = l[i] + l[i+1]
    l.append(s)

for k in (l):
    print(k)
