n = int(input("Enter the lenght of the list "))
x = 0
l = []
for i in range(n):
    x = input("Enter the values of the list ")
    l.append(x)
s = []
i = int(input("enter how many word you want to shift "))
for j in range(-1, -((len(l)-i)+1), -1):
    s.append(l[j])
for k in range(i):
    s.append(l[k])
print(s)
