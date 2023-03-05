a = int(input("Enter a number to check weather prime or not "))
f = 0
for i in range(2, a):
    if (a % i == 0):
        f = 1
        break

if f == 1:
    print("It is not a prime number")
else:
    print("It is a prime number")
