a = []

n = int(input("Enter the number of elements you want to check : "))

for i in range (n):
    s = int(input(f"Enter the {i+1} element "))
    a.append(s)
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
        print(f"The number {a[flag]} is a armstrong number")
    else:
        print(f"The number {a[flag]} is NOT a armstrong number")
    
    res = 0
        
    flag += 1