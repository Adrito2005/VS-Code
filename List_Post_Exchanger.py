n = int(input("Enter the length of the list want to enter "))

l = []

for i in range(n):
    p = input(f"Enter element number {i+1}: ")
    l.append(p)

for i in range(1, len(l), 2):
    l[i], l[i-1] = l[i-1], l[i]

print(l)
