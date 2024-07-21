x = int(input("Enter a number "))
p = []
z = []
flag = 0
s = 0
l = 0

for i in range(len(str(x))):
    p.append(x%10)
    x = x//10




p.sort()
for k in p:
    s = s * 10 +k
    l = int(str(s)[::-1])
    flag = flag+1
if(len(str(x)) != len(str(l))):
    l = l*(10**(int(len(str(l))))- int(len(str(x))+1))
    
for i in range(s,l+1):
    a = i
    for j in range(len(str(i))):
        z.append(a%10)
        a = a//10
    z.sort()
    if(z == p):
        print(i)
    z = []