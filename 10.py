a = int(input("Enter the number whose digits you want to add "))
s = 0
for i in str(a):
    s += int(i)

print(s)
