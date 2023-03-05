a = input("Enter the length of the list ")
l = []
for i in range(a):
    x = input("Enter the ", i+1, "th element ")
    l.append(x)

s = 0
res = 0
sum = 0

for i in l:
    s = len(str(i))
    k = i
    while k > 0:
        t1 = k % 10
        res = res + t1**s
        k = k//10
    k = 0
    if res == i:
        sum += i
    res = 0
print(sum)
