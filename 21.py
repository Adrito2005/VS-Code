a = int(input("Enter the length of the list "))

l = []

for i in range(a):
    x = input("Enter the element ")
    l.append(x)

for i in range(1, len(l), 2):
    l[i-1], l[i] = l[i], l[i-1]


print(l)
