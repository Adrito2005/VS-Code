n = int(input("Enter the ength of the list that you want to enter "))

l = []

for i in range(n):
    x = input("Enter the element of the list ")
    l.append(x)
    x = 0
s = ""
for k in l:
    if (len(s) < len(k)):
        s = k

print(s)
