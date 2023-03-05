a = int(input("Enter the length of the list "))
l = []
for i in range(a):
    x = input("Enter the tupples of the list ")
    l.append(a)


s = l[0]
for i in l:
    x = len(i)
    if x < len(s):
        s = i
print("Smallest tuple", len(s))
