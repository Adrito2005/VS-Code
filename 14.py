a = int(input("Enter a number to check weather it is spy or not "))
s = 0
p = 1
for i in list(str(a)):
    s += int(i)
    p = p*int(i)

if s == p:
    print("It is a spy number")
else:
    print("It is not a spy number")
