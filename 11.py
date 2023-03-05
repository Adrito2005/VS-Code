a = input("Enter the length of the list ")
l = []
for i in range(a):
    x = input("Enter the ", i+1, "th element ")
    l.append(x)

s = l[len(l)//2:]+l[0:len(l)//2]

print("swapped list = ", s)
