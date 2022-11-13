a = []

n = int(input("Enter the number of elements you want to check : "))
lines = []


for i in range (n):
    a.append(i)
res = 0
flag = 0
for j in a:
    l = len(str(j))
    for k in range (l):
        x = j%10
        j = j//10
        
        res = res + x**l
    j = 0
    x = 0
    
    if (res == a[flag]):
        lines.append(str(a[flag]))
    
    res = 0
        
    flag += 1
with open('readme.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')